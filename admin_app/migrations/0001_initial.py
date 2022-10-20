# Generated by Django 4.1.1 on 2022-10-11 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('dept_id', models.IntegerField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField(choices=[('CSE', 'CSE'), ('EEE', 'EEE'), ('SWE', 'SWE'), ('MCE', 'ME'), ('IPE', 'IPE'), ('CEE', 'CEE'), ('BTM', 'BTM')], max_length=30)),
            ],
        ),
    ]