# Generated by Django 5.0.6 on 2024-07-09 17:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("community", "0003_scrabpost_content_scrabpost_post_picture_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="scrabpost",
            name="content",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="scrabpost",
            name="post_picture",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="scrabpost",
            name="title",
            field=models.CharField(max_length=255),
        ),
    ]
