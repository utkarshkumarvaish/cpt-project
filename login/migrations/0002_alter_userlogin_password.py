# Generated by Django 4.2.2 on 2023-10-01 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogin',
            name='password',
            field=models.BinaryField(),
        ),
    ]
