# Generated by Django 4.0.4 on 2022-04-28 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0018_productreview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wholesaleproductorders',
            name='user',
        ),
        migrations.DeleteModel(
            name='WholeSaleProduct',
        ),
        migrations.DeleteModel(
            name='WholeSaleProductOrders',
        ),
    ]
