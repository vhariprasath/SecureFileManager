# Generated by Django 3.0.7 on 2021-07-04 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encdec', '0002_product_user_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user_key',
        ),
    ]
