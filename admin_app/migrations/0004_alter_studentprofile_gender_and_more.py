# Generated by Django 4.0.3 on 2022-10-14 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0003_studentprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='gender',
            field=models.CharField(choices=[('Female', 'FEMALE'), ('Male', 'MALE')], max_length=30),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='semester',
            field=models.IntegerField(choices=[(2, '2'), (4, '4'), (8, '8'), (6, '6'), (3, '3'), (5, '5'), (7, '7'), (1, '1')], default=1),
        ),
    ]
