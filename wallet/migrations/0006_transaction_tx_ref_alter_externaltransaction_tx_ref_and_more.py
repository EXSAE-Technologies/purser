# Generated by Django 4.1.5 on 2023-01-15 12:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0005_externaltransaction_alter_wallet_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='tx_ref',
            field=models.UUIDField(default=uuid.UUID('7a52c799-b8c3-476c-8745-f4ed1ac58412'), editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='externaltransaction',
            name='tx_ref',
            field=models.CharField(editable=False, max_length=200),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='id',
            field=models.UUIDField(default=uuid.UUID('28b58d64-4b08-4c37-81e2-192c09a8b98f'), editable=False, primary_key=True, serialize=False),
        ),
    ]