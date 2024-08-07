# Generated by Django 5.0.6 on 2024-07-08 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User_Question",
            fields=[
                ("question_id", models.AutoField(primary_key=True, serialize=False)),
                ("content", models.TextField()),
                ("answer", models.TextField()),
                (
                    "kakao_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.user"
                    ),
                ),
            ],
        ),
    ]
