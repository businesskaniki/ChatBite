# Generated by Django 3.2.18 on 2023-03-30 22:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="userprofile",
            managers=[],
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="background_image",
            field=models.ImageField(
                blank=True,
                default="images/profile/defualts/defualt_background.png",
                null=True,
                upload_to="images/profile/background_pictures",
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="profile_frmae",
            field=models.ImageField(
                blank=True,
                default="images/profile/defualts/defualt_frame.png",
                null=True,
                upload_to="",
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="profile_image",
            field=models.ImageField(
                blank=True,
                default="images/profile/defualts/defualt_profile.png",
                null=True,
                upload_to="images/profile/background_pictures",
            ),
        ),
    ]
