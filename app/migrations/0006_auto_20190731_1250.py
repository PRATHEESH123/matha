# Generated by Django 2.2.3 on 2019-07-31 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190731_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tble',
            name='discription',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='tble',
            name='tittle',
            field=models.CharField(default='', max_length=50),
        ),
    ]
