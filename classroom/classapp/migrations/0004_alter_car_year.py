# Generated by Django 5.0.3 on 2024-04-22 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classapp', '0003_signupform_rename_login_loginform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.DateField(max_length=100),
        ),
    ]