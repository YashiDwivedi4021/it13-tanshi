# Generated by Django 5.0.1 on 2024-02-24 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_contactenquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactenquiry',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
