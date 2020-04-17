# Generated by Django 3.0.5 on 2020-04-15 23:12

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, default='', upload_to=shop.models.get_upload_path_thumb),
        ),
    ]