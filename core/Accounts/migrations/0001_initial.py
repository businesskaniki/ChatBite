# Generated by Django 4.1.7 on 2023-03-20 12:25

import Accounts.models
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=200, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date_joined')),
                ('last_seen', models.DateTimeField(auto_now=True, verbose_name='last_seen')),
                ('profile_image', models.ImageField(blank=True, default=Accounts.models.defualt_profile, null=True, upload_to=Accounts.models.upload_loc)),
                ('background_image', models.ImageField(blank=True, default=Accounts.models.defualt_backgroung, null=True, upload_to=Accounts.models.upload_loc)),
                ('profile_frmae', models.ImageField(blank=True, default=Accounts.models.defualt_profile_frame, null=True, upload_to='')),
                ('bite_credit', models.IntegerField(default=0)),
                ('about', models.CharField(blank=True, max_length=300, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=12, null=True)),
                ('tire', models.CharField(default='rokie', max_length=20)),
                ('blocked', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]