from django.contrib import admin
from ducats.accounts.models import Account

class AccountAdmin(admin.ModelAdmin):
    pass

admin.site.register(Account, AccountAdmin)
