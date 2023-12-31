# Generated by Django 4.2.6 on 2023-11-21 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoint', '0004_receipt_product_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='email',
        ),
        migrations.AddField(
            model_name='client',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='client',
            name='orders',
            field=models.ManyToManyField(to='endpoint.receipt'),
        ),
    ]
