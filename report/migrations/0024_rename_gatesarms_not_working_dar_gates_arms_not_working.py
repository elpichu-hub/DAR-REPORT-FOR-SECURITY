# Generated by Django 3.2.3 on 2021-05-25 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0023_auto_20210525_1515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dar',
            old_name='gatesarms_not_working',
            new_name='gates_arms_not_working',
        ),
    ]
