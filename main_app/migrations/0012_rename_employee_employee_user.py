# Generated by Django 4.1.2 on 2022-10-29 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_alter_moduleteam_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='employee',
            new_name='user',
        ),
    ]
