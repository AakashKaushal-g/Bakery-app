# Generated by Django 4.1.3 on 2022-11-26 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.FloatField(default=0),
        ),
    ]
