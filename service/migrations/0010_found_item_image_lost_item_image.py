# Generated by Django 5.0.1 on 2024-03-30 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_alter_contactenquiry_id_alter_found_item_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='found_item',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
        migrations.AddField(
            model_name='lost_item',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]
