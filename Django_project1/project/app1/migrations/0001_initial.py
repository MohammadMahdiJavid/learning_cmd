# Generated by Django 2.2.5 on 2019-10-29 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command1', models.CharField(max_length=200)),
                ('command2', models.CharField(max_length=200)),
                ('lesson', models.CharField(max_length=200)),
            ],
        ),
    ]