# Generated by Django 2.1 on 2018-08-07 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywaitfree', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='group_size',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]