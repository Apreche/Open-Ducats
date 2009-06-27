from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    description = models.TextField()
    owner = models.ForeignKey(User)
    balance = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    STATUS_OPTIONS = (
        ('A', 'Active'),
        ('I', 'Inactive'),
    )
    status = models.CharField(max_length=1, choices=STATUS_OPTIONS)
