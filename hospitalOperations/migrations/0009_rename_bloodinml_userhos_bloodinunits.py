# Generated by Django 4.2.2 on 2023-10-18 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalOperations', '0008_alter_userhos_date_of_sent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userhos',
            old_name='BloodInMl',
            new_name='BloodInUnits',
        ),
    ]