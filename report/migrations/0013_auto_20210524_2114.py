# Generated by Django 3.2.3 on 2021-05-25 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0012_alter_daradditionalcomment_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dar',
            name='officer_to_relieve',
        ),
        migrations.AddField(
            model_name='daradditionalcomment',
            name='officer_to_relieve',
            field=models.CharField(default='Burchfield', max_length=30),
        ),
        migrations.AlterField(
            model_name='daradditionalcomment',
            name='time',
            field=models.CharField(default='13:00', max_length=50),
        ),
    ]
