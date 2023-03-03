# Generated by Django 4.1.5 on 2023-03-03 18:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0009_alter_wallet_id_alter_wallet_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='currency',
            field=models.CharField(choices=[('zmw', 'ZMW')], default='zmw', max_length=200),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='id',
            field=models.UUIDField(default=uuid.UUID('7b838b20-fcea-4510-8e6e-4136abe40ea5'), editable=False, primary_key=True, serialize=False),
        ),
    ]