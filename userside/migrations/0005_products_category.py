# Generated by Django 5.2.3 on 2025-06-21 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('all', 'All'), ('phones', 'Phones'), ('toys', 'Toys'), ('watches', 'Watches'), ('electronics', 'Electronics')], default='all', max_length=50),
        ),
    ]
