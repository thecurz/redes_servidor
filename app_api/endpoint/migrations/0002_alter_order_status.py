# Generated by Django 4.2.6 on 2023-10-31 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoint', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='pending', max_length=50),
        ),
    ]
