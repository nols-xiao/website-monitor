# Generated by Django 2.2.5 on 2021-07-09 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_auto_20210709_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='username',
            name='alisname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]