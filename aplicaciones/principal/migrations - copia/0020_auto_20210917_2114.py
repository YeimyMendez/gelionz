# Generated by Django 3.1.7 on 2021-09-18 02:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0019_auto_20210917_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='perfil_FK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
