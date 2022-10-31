# Generated by Django 4.1.2 on 2022-10-31 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0004_rename_cart_id_cartitem_cart_remove_cartitem_product"),
        ("purchase", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="purchasedlist",
            name="product",
        ),
        migrations.AddField(
            model_name="purchasedlist",
            name="cart",
            field=models.OneToOneField(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="cart.cart"
            ),
            preserve_default=False,
        ),
    ]
