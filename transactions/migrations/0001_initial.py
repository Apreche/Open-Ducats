
from south.db import db
from django.db import models
from transactions.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Transaction'
        db.create_table('transactions_transaction', (
            ('timestamp', models.DateTimeField(auto_now_add=True)),
            ('notes', models.TextField()),
            ('amount', models.PositiveIntegerField()),
            ('template', models.ForeignKey(orm.TransactionTemplate)),
            ('receiver', models.ForeignKey(orm['accounts.Account'], related_name='real_receiver')),
            ('id', models.AutoField(primary_key=True)),
            ('giver', models.ForeignKey(orm['accounts.Account'], related_name='real_giver')),
        ))
        db.send_create_signal('transactions', ['Transaction'])
        
        # Adding model 'TransactionTemplate'
        db.create_table('transactions_transactiontemplate', (
            ('default_amount', models.PositiveIntegerField(null=True, blank=True)),
            ('last_used', models.DateTimeField()),
            ('description', models.TextField()),
            ('creator', models.ForeignKey(orm['auth.User'])),
            ('created_at', models.DateTimeField(auto_now_add=True)),
            ('id', models.AutoField(primary_key=True)),
            ('default_receiver', models.ForeignKey(orm['accounts.Account'], related_name='default_receiver', blank=True)),
            ('status', models.CharField(max_length=1)),
            ('default_giver', models.ForeignKey(orm['accounts.Account'], related_name='default_giver', blank=True)),
            ('slug', models.SlugField(max_length=250)),
            ('name', models.CharField(max_length=200)),
        ))
        db.send_create_signal('transactions', ['TransactionTemplate'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Transaction'
        db.delete_table('transactions_transaction')
        
        # Deleting model 'TransactionTemplate'
        db.delete_table('transactions_transactiontemplate')
        
    
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'transactions.transaction': {
            'amount': ('models.PositiveIntegerField', [], {}),
            'giver': ('models.ForeignKey', ['Account'], {'related_name': "'real_giver'"}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'notes': ('models.TextField', [], {}),
            'receiver': ('models.ForeignKey', ['Account'], {'related_name': "'real_receiver'"}),
            'template': ('models.ForeignKey', ["'TransactionTemplate'"], {}),
            'timestamp': ('models.DateTimeField', [], {'auto_now_add': 'True'})
        },
        'accounts.account': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'transactions.transactiontemplate': {
            'created_at': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'creator': ('models.ForeignKey', ['User'], {}),
            'default_amount': ('models.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'default_giver': ('models.ForeignKey', ['Account'], {'related_name': "'default_giver'", 'blank': 'True'}),
            'default_receiver': ('models.ForeignKey', ['Account'], {'related_name': "'default_receiver'", 'blank': 'True'}),
            'description': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'last_used': ('models.DateTimeField', [], {}),
            'name': ('models.CharField', [], {'max_length': '200'}),
            'slug': ('models.SlugField', [], {'max_length': '250'}),
            'status': ('models.CharField', [], {'max_length': '1'})
        }
    }
    
    complete_apps = ['transactions']
