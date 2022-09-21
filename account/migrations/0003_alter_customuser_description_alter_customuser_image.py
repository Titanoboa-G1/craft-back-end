# Generated by Django 4.1.1 on 2022-09-21 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_alter_customuser_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="craftsmen_images/"
            ),
        ),
    ]