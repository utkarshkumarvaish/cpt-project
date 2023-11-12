# Generated by Django 4.2.2 on 2023-09-30 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=128)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=1500)),
                ('state', models.CharField(max_length=1500)),
                ('country', models.CharField(max_length=1500)),
                ('postal_code', models.CharField(max_length=150)),
                ('country_code', models.CharField(max_length=10)),
                ('locality', models.CharField(max_length=1500)),
                ('phone_number', models.CharField(max_length=15)),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=4)),
                ('location', models.CharField(max_length=1500)),
                ('last_logiend', models.DateTimeField(auto_now_add=True)),
                ('last_logined_location', models.CharField(max_length=1500)),
                ('updated_loction', models.CharField(max_length=1500)),
                ('dob', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.userlogin')),
            ],
        ),
    ]
