# Generated by Django 4.1.2 on 2022-11-23 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smbapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instrument',
            old_name='nmae',
            new_name='name',
        ),
    ]
