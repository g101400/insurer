# Generated by Django 3.1.3 on 2021-01-04 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0004_auto_20210104_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insurancepolicy',
            name='sms',
        ),
        migrations.AddField(
            model_name='insurancepolicy',
            name='sms',
            field=models.ManyToManyField(blank=True, null=True, to='customer_service.MessageSms'),
        ),
    ]
