# Generated by Django 3.2.3 on 2021-05-24 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0009_daradditionalcomment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daradditionalcomment',
            name='time',
            field=models.CharField(default='13:00', max_length=50),
        ),
    ]
