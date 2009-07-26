from django.views.generic.list_detail import object_list, object_detail

from ducats.transactions.models import TransactionTemplate, Transaction

def template_list(request):
    templates = TransactionTemplate.objects.all()
    return object_list( request, templates )

def transaction_log( request, template ):
    transactions = Transaction.objects.filter(template__slug=template)
    return object_list( request, transactions )
