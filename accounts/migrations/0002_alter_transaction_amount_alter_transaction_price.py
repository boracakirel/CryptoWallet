# Generated by Django 4.1.2 on 2022-10-31 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=10, max_digits=100),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='price',
            field=models.DecimalField(decimal_places=10, max_digits=100),
        ),
    ]
