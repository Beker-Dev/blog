# Generated by Django 4.0.6 on 2022-07-14 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='published',
            new_name='is_published',
        ),
    ]