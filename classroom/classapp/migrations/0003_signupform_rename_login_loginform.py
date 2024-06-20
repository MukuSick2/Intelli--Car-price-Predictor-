# Generated by Django 5.0.4 on 2024-04-21 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classapp', '0002_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='signupForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=8)),
            ],
        ),
        migrations.RenameModel(
            old_name='login',
            new_name='LoginForm',
        ),
    ]
