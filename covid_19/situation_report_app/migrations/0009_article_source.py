# Generated by Django 3.0.3 on 2020-03-13 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('situation_report_app', '0008_auto_20200313_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='source',
            field=models.CharField(max_length=16, null=True),
        ),
    ]