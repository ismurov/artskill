# Generated by Django 2.1.7 on 2019-03-05 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0013_auto_20170821_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='details_description',
            field=models.TextField(blank=True, verbose_name='Details description'),
        ),
    ]
