# Generated by Django 4.1.6 on 2023-02-13 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("professionals", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Agenda",
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
                ("day", models.DateField()),
                (
                    "start_time",
                    models.CharField(
                        choices=[
                            ("8:00", "8:00 AM"),
                            ("8:30", "8:30 AM"),
                            ("9:00", "9:00 AM"),
                            ("9:30", "9:30 AM"),
                            ("10:00", "10:00 AM"),
                            ("10:30", "10:30 AM"),
                            ("11:00", "11:00 AM"),
                            ("11:30", "11:30 AM"),
                            ("12:00", "12:00 PM"),
                            ("12:30", "12:30 PM"),
                            ("13:00", "13:00 PM"),
                            ("13:30", "13:30 PM"),
                            ("14:00", "14:00 PM"),
                            ("14:30", "14:30 PM"),
                            ("15:00", "15:00 PM"),
                            ("15:30", "15:30 PM"),
                            ("16:00", "16:00 PM"),
                            ("16:30", "16:30 PM"),
                            ("17:00", "17:00 PM"),
                            ("17:30", "17:30 PM"),
                            ("18:00", "18:00 PM"),
                            ("18:30", "18:30 PM"),
                            ("19:00", "19:00 PM"),
                            ("19:30", "19:30 PM"),
                        ],
                        max_length=5,
                    ),
                ),
                (
                    "end_time",
                    models.CharField(
                        choices=[
                            ("8:30", "8:30 AM"),
                            ("9:00", "9:00 AM"),
                            ("9:30", "9:30 AM"),
                            ("10:00", "10:00 AM"),
                            ("10:30", "10:30 AM"),
                            ("11:00", "11:00 AM"),
                            ("11:30", "11:30 AM"),
                            ("12:00", "12:00 PM"),
                            ("12:30", "12:30 PM"),
                            ("13:00", "13:00 PM"),
                            ("13:30", "13:30 PM"),
                            ("14:00", "14:00 PM"),
                            ("14:30", "14:30 PM"),
                            ("15:00", "15:00 PM"),
                            ("15:30", "15:30 PM"),
                            ("16:00", "16:00 PM"),
                            ("16:30", "16:30 PM"),
                            ("17:00", "17:00 PM"),
                            ("17:30", "17:30 PM"),
                            ("18:00", "18:00 PM"),
                            ("18:30", "18:30 PM"),
                            ("19:00", "19:00 PM"),
                            ("19:30", "19:30 PM"),
                            ("20:00", "20:00 PM"),
                        ],
                        max_length=5,
                    ),
                ),
                ("available", models.BooleanField(default=True)),
                (
                    "professional",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="professionals.professional",
                    ),
                ),
            ],
        ),
    ]
