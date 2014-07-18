# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PeriodClose.bot_closed'
        db.add_column(u'Invoices_periodclose', 'bot_closed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PeriodClose.bot_closed'
        db.delete_column(u'Invoices_periodclose', 'bot_closed')


    models = {
        u'Invoices.client': {
            'CIF': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Client'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'otherCIF': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'Invoices.coop': {
            'Meta': {'object_name': 'Coop'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'db_index': 'True'})
        },
        u'Invoices.csvimport': {
            'Meta': {'object_name': 'CSVImport'},
            'encoding': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'error_log': ('django.db.models.fields.TextField', [], {}),
            'field_list': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'file_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'import_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'import_user': ('django.db.models.fields.CharField', [], {'default': "'anonymous'", 'max_length': '255', 'blank': 'True'}),
            'model_name': ('django.db.models.fields.CharField', [], {'default': "'iisharing.Item'", 'max_length': '255'}),
            'upload_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'upload_method': ('django.db.models.fields.CharField', [], {'default': "'manual'", 'max_length': '50'})
        },
        u'Invoices.email': {
            'Meta': {'object_name': 'Email'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'efrom': ('django.db.models.fields.EmailField', [], {'default': "'gee@gestion.org'", 'max_length': '75'}),
            'eto': ('django.db.models.fields.CharField', [], {'default': "'camp reservat pel sistema'", 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'Invoices.emailnotification': {
            'Meta': {'object_name': 'EmailNotification', '_ormbases': [u'Invoices.Email']},
            u'email_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['Invoices.Email']", 'unique': 'True', 'primary_key': 'True'}),
            'ento': ('django.db.models.fields.IntegerField', [], {}),
            'notification_type': ('django.db.models.fields.IntegerField', [], {}),
            'offset_days': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'period': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Invoices.period']"}),
            'pointed_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 7, 16, 0, 0)'}),
            'sent_to_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'Invoices.paymententities': {
            'Meta': {'object_name': 'paymentEntities'},
            'concept': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'entity': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'Invoices.period': {
            'Meta': {'object_name': 'period'},
            'date_close': ('django.db.models.fields.DateField', [], {}),
            'date_open': ('django.db.models.fields.DateField', [], {}),
            'first_day': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'Invoices.periodclose': {
            'CESnumber': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'Meta': {'unique_together': "(('user', 'period'),)", 'object_name': 'PeriodClose'},
            'Purchases_IRPFRetention': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'Purchases_expencedVAT': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'Purchases_total': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'Purchases_totalVAT': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'Sales_assignedVAT': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'Sales_invoicedVAT': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'Sales_total': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'Sales_totalVAT': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'Savings_donation': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2'}),
            'VAT_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'bot_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'donation_eco': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '7', 'decimal_places': '2'}),
            'donation_euro': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '7', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment_entity': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'payment'", 'symmetrical': 'False', 'to': u"orm['Invoices.paymentEntities']"}),
            'period': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Invoices.period']", 'blank': 'True'}),
            'periodTAX': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'periodTAXeco': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2'}),
            'periodTAXeuro': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2'}),
            'preTAX': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'refund_entity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Invoices.refundEntities']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'Invoices.periodtaxes': {
            'Meta': {'object_name': 'periodTaxes'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_base': ('django.db.models.fields.IntegerField', [], {}),
            'min_base': ('django.db.models.fields.IntegerField', [], {}),
            'taxId': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'db_index': 'True'})
        },
        u'Invoices.provider': {
            'CIF': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Provider'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'otherCIF': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'Invoices.purchaseinvoice': {
            'Meta': {'unique_together': "(('user', 'period', 'num', 'percentExpencedVAT'),)", 'object_name': 'PurchaseInvoice'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'percentExpencedVAT': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Invoices.VATS']"}),
            'percentIRPFRetention': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'period': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['Invoices.period']"}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Invoices.Provider']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '65', 'decimal_places': '2'})
        },
        u'Invoices.refundentities': {
            'Meta': {'object_name': 'refundEntities'},
            'concept': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'entity': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'Invoices.salesinvoice': {
            'Meta': {'unique_together': "(('user', 'period', 'num', 'percentInvoicedVAT'),)", 'object_name': 'SalesInvoice'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Invoices.Client']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'percentInvoicedVAT': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Invoices.VATS']"}),
            'period': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['Invoices.period']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        u'Invoices.soci': {
            'IVA_assignat': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'Meta': {'object_name': 'Soci'},
            'coop': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Invoices.Coop']"}),
            'coop_number': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'max_length': '4', 'db_index': 'True'}),
            'extra_days': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'preTAX': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'Invoices.vats': {
            'Meta': {'object_name': 'VATS'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'db_index': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['Invoices']