# Generated by Django 2.1.7 on 2023-06-19 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TO_DO_APP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('C', 'Complete'), ('P', 'PENDING')], max_length=2),
        ),
    ]
