from django.contrib import admin
from ducats.transactions.models import TransactionTemplate, Transaction

class TransactionTemplateAdmin(admin.ModelAdmin):
    pass

class TransactionAdmin(admin.ModelAdmin):
    pass

admin.site.register(TransactionTemplate, TransactionTemplateAdmin)
admin.site.register(Transaction, TransactionAdmin)
