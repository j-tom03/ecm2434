# Generated by Django 4.2.11 on 2024-03-18 20:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("challenges", "0005_alter_user_profile_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="profile_image",
        ),
        migrations.AddField(
            model_name="user",
            name="image",
            field=models.CharField(default="dog", max_length=200),
        ),
    ]
