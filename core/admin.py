from django.contrib import admin

from core.models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    resource_class = Transaction
    list_filter = [
        "transaction_status",
        "sender",
        "receiver",
    ]
    search_fields = (
        "transaction_uuid",
    )
    list_display = ('sender', 'receiver', 'transaction_uuid', 'transaction_status', 'created_at', 'updated_at')


admin.site.register(Transaction, TransactionAdmin)
