# Generated by Django 2.2.1 on 2019-06-05 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0004_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='avatar',
            field=models.CharField(max_length=10),
        ),
    ]
