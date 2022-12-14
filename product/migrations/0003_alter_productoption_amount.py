# Generated by Django 4.1.2 on 2022-10-31 10:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_alter_product_description_alter_product_is_public_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productoption",
            name="amount",
            field=models.IntegerField(
                blank=True,
                help_text="재고량을 입력하세요.",
                validators=[django.core.validators.MinValueValidator(0)],
            ),
        ),
    ]
