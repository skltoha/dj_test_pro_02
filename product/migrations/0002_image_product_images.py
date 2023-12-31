# Generated by Django 4.2.2 on 2023-06-23 02:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
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
                ("image", models.ImageField(upload_to="images/")),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="images",
            field=models.ManyToManyField(to="product.image"),
        ),
    ]
