# Generated by Django 3.1.6 on 2021-05-06 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacationrequests',
            name='first_name',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='vacationrequests',
            name='last_name',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='vacationrequests',
            name='postGradLevel',
            field=models.CharField(choices=[('1', 'PGY1'), ('2', 'PGY2'), ('3', 'PGY3'), ('4', 'PGY4'), ('5', 'PGY5')], default='', max_length=4),
        ),
    ]