# Generated by Django 3.2.16 on 2023-01-09 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dssProject', '0009_auto_20230103_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='grupo',
            field=models.CharField(max_length=500),
        ),
    ]
