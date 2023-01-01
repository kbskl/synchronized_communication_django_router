from django.db import models
from django.utils import timezone

from core.util.constant import TransactionStatusEnum


class General(models.Model):
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(editable=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()

        self.updated_at = timezone.now()
        return super(General, self).save(*args, **kwargs)


class Transaction(General):
    sender = models.CharField(max_length=255, null=True, blank=True)
    receiver = models.CharField(max_length=255, null=True, blank=True)
    transaction_uuid = models.CharField(max_length=255, null=True, blank=True)
    transaction_status = models.CharField(choices=TransactionStatusEnum.choices(), blank=True, null=True, max_length=50,
                                          default=TransactionStatusEnum.in_router.value)
    data = models.TextField(null=True, blank=True)

