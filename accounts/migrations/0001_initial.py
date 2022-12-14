# Generated by Django 4.1.2 on 2022-10-31 20:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=100, max_digits=100)),
                ('quantity', models.IntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=100, max_digits=100)),
                ('coin_id', models.CharField(max_length=100, unique=True)),
                ('user_id', models.ManyToManyField(blank=True, related_name='coins_in_wallet', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
