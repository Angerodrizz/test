# Generated by Django 2.0.3 on 2020-06-22 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_auto_20200622_1023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='name',
            new_name='title',
        ),
    ]