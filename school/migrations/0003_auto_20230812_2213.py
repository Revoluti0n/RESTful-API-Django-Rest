# Generated by Django 3.0.7 on 2023-08-13 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20230812_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('B', 'Basic'), ('A', 'Advanced'), ('I', 'Intermediate')], default='B', max_length=1),
        ),
    ]
