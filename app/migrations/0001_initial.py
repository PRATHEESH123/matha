# Generated by Django 2.2.3 on 2019-07-30 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=50)),
                ('img1', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='file')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='file')),
                ('img3', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='file')),
                ('discription', models.CharField(max_length=50)),
            ],
        ),
    ]
