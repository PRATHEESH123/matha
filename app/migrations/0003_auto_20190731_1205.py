# Generated by Django 2.2.3 on 2019-07-31 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190731_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='tble',
            name='discription1',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='tble',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='file'),
        ),
        migrations.AddField(
            model_name='tble',
            name='tittle1',
            field=models.CharField(default='', max_length=50),
        ),
    ]
