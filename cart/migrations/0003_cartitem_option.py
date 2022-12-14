# Generated by Django 4.1.2 on 2022-10-28 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_alter_product_description_alter_product_is_public_and_more"),
        ("cart", "0002_remove_cart_is_present_remove_cart_product_cartitem"),
    ]

    operations = [
        migrations.AddField(
            model_name="cartitem",
            name="option",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="product.productoption",
            ),
            preserve_default=False,
        ),
    ]
