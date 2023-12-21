# Generated by Django 4.2.7 on 2023-12-21 00:27

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("party", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Party",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("party_date", models.DateField()),
                ("party_time", models.TimeField()),
                ("invitation", models.TextField()),
                ("venue", models.CharField(max_length=200)),
                (
                    "organizer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="organized_parties",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "parties",
            },
        ),
        migrations.CreateModel(
            name="Guest",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("attending", models.BooleanField(default=False)),
                (
                    "party",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="guests",
                        to="party.party",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Gift",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("gift", models.CharField(max_length=200)),
                ("price", models.FloatField(blank=True, null=True)),
                ("link", models.URLField(blank=True, null=True)),
                (
                    "party",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="party.party"
                    ),
                ),
            ],
        ),
    ]
