from django.views.generic.list_detail import object_detail, object_list
from django.contrib.auth.decorators import login_required

from ducats.accounts.models import Account

def account_detail( request, slug ):
    accounts = Account.objects.all()
    return object_detail( request, accounts, slug=slug )

@login_required
def owned_account_list( request ):
    accounts = Account.objects.filter(owner=request.user)
    return object_list( request, accounts )
