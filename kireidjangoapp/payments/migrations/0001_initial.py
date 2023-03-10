# Generated by Django 4.1.6 on 2023-02-13 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=6)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "payment_method",
                    models.CharField(
                        choices=[
                            ("credit_card", "Tarjeta de crédito"),
                            ("debit_card", "Tarjeta de débito"),
                            ("cash", "Efectivo"),
                            ("bank_transfer", "Transferencia bancaria"),
                            ("mercado_pago", "Mercado Pago"),
                            ("other", "Otro"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pendiente"),
                            ("success", "Exitosa"),
                            ("failed", "Fallida"),
                            ("refunded", "Reembolsada"),
                            ("cancelled", "Cancelada"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="orders.order"
                    ),
                ),
            ],
        ),
    ]
