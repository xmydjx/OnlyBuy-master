# Generated by Django 2.1.3 on 2019-05-17 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberapp', '0004_auto_20190517_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='listimg',
            field=models.ImageField(default='', upload_to='list', verbose_name='列表页图'),
        ),
    ]
