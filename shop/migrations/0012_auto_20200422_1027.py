# Generated by Django 3.0.5 on 2020-04-22 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20200422_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsize',
            name='sizesInStock',
        ),
        migrations.AddField(
            model_name='productsize',
            name='sizeInStock',
            field=models.IntegerField(default=1),
        ),
    ]
