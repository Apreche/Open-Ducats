from django.db import models
from django.contrib.auth.models import User

from ducats.accounts.models import Account

class TransactionTemplate(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    description = models.TextField()
    creator = models.ForeignKey(User)
    default_giver = models.ForeignKey(Account,blank=True,related_name='default_giver')
    default_receiver = models.ForeignKey(Account,blank=True,related_name='default_receiver')
    default_amount = models.PositiveIntegerField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField()

    STATUS_OPTIONS = (
        ('A', 'Active'),
        ('I', 'Inactive'),
    )
    status = models.CharField(max_length=1, choices=STATUS_OPTIONS)

    def __unicode__(self):
        return self.name

class Transaction(models.Model):
    template = models.ForeignKey('TransactionTemplate')
    notes = models.TextField()
    giver = models.ForeignKey(Account,related_name='real_giver')
    receiver = models.ForeignKey(Account,related_name='real_receiver')
    amount = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s %s %s:%s %s" % (self.template.name, self.timestamp, self.giver, self.receiver, self.amount )
