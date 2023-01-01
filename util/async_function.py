import json

from asgiref.sync import sync_to_async

from core.models import Transaction


@sync_to_async
def create_transaction(receiver, sender, uuid, data):
    Transaction.objects.create(receiver=receiver, transaction_uuid=uuid, sender=sender, data=json.dumps(data))


@sync_to_async
def update_transaction_status(transaction_status, uuid):
    Transaction.objects.filter(transaction_uuid=uuid).update(transaction_status=transaction_status)
