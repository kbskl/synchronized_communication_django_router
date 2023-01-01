from enum import Enum


class GeneralEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((i.value, i.value) for i in cls)

    @classmethod
    def choice_2(cls):
        return tuple((i.value, i.name) for i in cls)

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class TransactionStatusEnum(GeneralEnum):
    in_router = "Reached the router"
    in_receiver = "Reached the receiver"
