# Generated by Django 4.0.4 on 2022-04-28 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0024_remove_product_price_not'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsize',
            name='quantity',
        ),
    ]
