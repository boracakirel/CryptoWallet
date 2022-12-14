# Generated by Django 4.1.2 on 2022-10-31 22:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_alter_transaction_amount_alter_transaction_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='user_id',
        ),
        migrations.AddField(
            model_name='transaction',
            name='user',
            field=models.ManyToManyField(blank=True, related_name='transactions', to=settings.AUTH_USER_MODEL),
        ),
    ]
