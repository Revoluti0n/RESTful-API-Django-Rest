# Generated by Django 3.0.7 on 2023-08-13 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0023_auto_20230812_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='period',
            field=models.CharField(choices=[('M', 'Matutinal'), ('V', 'Vespertine'), ('N', 'Nocturnal')], default='M', max_length=1),
        ),
    ]
