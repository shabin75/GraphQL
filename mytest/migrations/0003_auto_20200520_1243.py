# Generated by Django 2.2 on 2020-05-20 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytest', '0002_auto_20200520_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='age',
            field=models.TextField(blank=True),
        ),
    ]
