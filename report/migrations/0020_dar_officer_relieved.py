# Generated by Django 3.2.3 on 2021-05-25 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0019_dar_additional_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='dar',
            name='officer_relieved',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
