# Generated by Django 4.2.5 on 2023-09-13 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('try2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='block',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='floor',
            field=models.IntegerField(null=True),
        ),
    ]
