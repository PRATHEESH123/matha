# Generated by Django 2.2.3 on 2019-07-31 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190731_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tble',
            name='img2',
            field=models.ImageField(blank=True, default='', upload_to='img', verbose_name='file'),
        ),
    ]
