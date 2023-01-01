import asyncio
import json
import threading
import aioredis
import async_timeout
from core.util.constant import TransactionStatusEnum
from util.async_function import create_transaction, update_transaction_status
from util.router_manager_config import CHANNELS, REDIS_PASSWORD, REDIS_URL


class RouteManager:
    def __init__(self):
        self.redis = None
        self.pubsub = None
        self.channels = CHANNELS

    async def __load(self):
        self.redis = aioredis.from_url(REDIS_URL, password=REDIS_PASSWORD)
        self.pubsub = self.redis.pubsub()

    async def __reader(self, channel: aioredis.client.PubSub):
        print("Reader starting...")
        while True:
            try:
                async with async_timeout.timeout(1):
                    message = await channel.get_message(ignore_subscribe_messages=True)
                    if message is not None:
                        data = json.loads(message['data'].decode())
                        if data.get('transaction_uuid', None) is not None:
                            await update_transaction_status(uuid=data.get('transaction_uuid'),
                                                            transaction_status=TransactionStatusEnum.in_receiver.value)
                            continue
                        if data.get('sender', None) is None:
                            continue
                        from_server = list(self.channels.keys())[
                            list(self.channels.values()).index(data['sender'])]
                        if from_server == data['to']:
                            continue
                        await create_transaction(receiver=data['to'], uuid=data['uuid'], sender=from_server,
                                                 data=data['data'])
                        await self.__publish(self.channels[data['to']],
                                             json.dumps(
                                                 {"from": from_server, "data": data['data'], "uuid": data['uuid']}))
                    await asyncio.sleep(0.01)
            except aioredis.exceptions.ConnectionError:
                print("Connection error. Sub Closed.")
                await asyncio.sleep(10)
                break
            except Exception as e:
                print(f"Error:{e}")
                continue

    def subscribe(self):
        def loop_in_thread(lp):
            asyncio.set_event_loop(lp)
            lp.run_until_complete(self.__subscribe())

        loop = asyncio.new_event_loop()
        t = threading.Thread(target=loop_in_thread, args=(loop,))
        t.start()

    async def __subscribe(self):
        await self.__load()
        await self.pubsub.subscribe(*self.channels.values())
        future = asyncio.create_task(self.__reader(self.pubsub))
        await future

    async def __publish(self, channel, data):
        await self.redis.publish(channel, data)
