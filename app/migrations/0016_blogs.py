# Generated by Django 2.2.3 on 2019-08-05 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=50)),
                ('img', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='file')),
                ('discription', models.CharField(max_length=50)),
                ('link', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
