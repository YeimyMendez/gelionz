# Generated by Django 3.2.7 on 2021-09-13 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0009_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile'),
        ),
    ]
