# Generated by Django 3.0.7 on 2023-08-13 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0018_auto_20230812_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('I', 'Intermediate'), ('B', 'Basic'), ('A', 'Advanced')], default='B', max_length=1),
        ),
    ]
