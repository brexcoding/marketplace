# Generated by Django 5.0.1 on 2024-01-12 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_order_alter_product_image_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.CharField(max_length=555),
        ),
    ]