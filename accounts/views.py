from django.views.generic.list_detail import object_detail
from accounts.models import Account

def account_detail( request, slug ):
    accounts = Account.objects.all()
    return object_detail( request, accounts, slug=slug )
