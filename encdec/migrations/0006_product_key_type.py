# Generated by Django 3.0.7 on 2021-08-03 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encdec', '0005_product_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='key_type',
            field=models.TextField(default='', max_length=100),
        ),
    ]
