# Generated by Django 3.0.4 on 2020-03-26 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200326_1659'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FeaturesLeft',
        ),
        migrations.DeleteModel(
            name='FeaturesRight',
        ),
    ]