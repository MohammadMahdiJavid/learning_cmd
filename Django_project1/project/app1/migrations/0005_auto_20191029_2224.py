# Generated by Django 2.2.5 on 2019-10-29 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_commands_command1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commands',
            name='command1',
            field=models.CharField(max_length=200),
        ),
    ]
