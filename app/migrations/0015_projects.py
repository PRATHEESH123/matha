# Generated by Django 2.2.3 on 2019-08-05 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20190802_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=50)),
                ('img', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='file')),
                ('discription', models.CharField(max_length=50)),
                ('link', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
