# Generated by Django 5.0 on 2024-01-10 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_address_remove_user_username_user_email_user_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
