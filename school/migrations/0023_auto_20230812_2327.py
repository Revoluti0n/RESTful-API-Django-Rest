# Generated by Django 3.0.7 on 2023-08-13 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0022_auto_20230812_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='period',
            field=models.CharField(choices=[('N', 'Nocturnal'), ('M', 'Matutinal'), ('V', 'Vespertine')], default='M', max_length=1),
        ),
    ]
