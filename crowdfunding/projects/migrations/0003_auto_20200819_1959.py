# Generated by Django 3.0.8 on 2020-08-19 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_pledge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pledge',
            old_name='annonymous',
            new_name='anonymous',
        ),
    ]
