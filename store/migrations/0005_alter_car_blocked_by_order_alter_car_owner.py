# Generated by Django 4.2.6 on 2023-10-25 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0004_remove_order_is_paid_remove_orderquantity_car_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="blocked_by_order",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="reserved_cars",
                to="store.order",
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="cars",
                to="store.client",
            ),
        ),
    ]