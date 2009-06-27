
from south.db import db
from django.db import models
from accounts.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Account'
        db.create_table('accounts_account', (
            ('status', models.CharField(max_length=1)),
            ('description', models.TextField()),
            ('created_at', models.DateTimeField(auto_now_add=True)),
            ('updated_at', models.DateTimeField(auto_now=True)),
            ('id', models.AutoField(primary_key=True)),
            ('owner', models.ForeignKey(orm['auth.User'])),
            ('balance', models.PositiveIntegerField()),
            ('slug', models.SlugField(max_length=250)),
            ('name', models.CharField(max_length=200)),
        ))
        db.send_create_signal('accounts', ['Account'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Account'
        db.delete_table('accounts_account')
        
    
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'accounts.account': {
            'balance': ('models.PositiveIntegerField', [], {}),
            'created_at': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'description': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '200'}),
            'owner': ('models.ForeignKey', ['User'], {}),
            'slug': ('models.SlugField', [], {'max_length': '250'}),
            'status': ('models.CharField', [], {'max_length': '1'}),
            'updated_at': ('models.DateTimeField', [], {'auto_now': 'True'})
        }
    }
    
    complete_apps = ['accounts']
