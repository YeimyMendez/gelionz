# Generated by Django 3.1.7 on 2021-09-18 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0022_auto_20210918_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='perfil_FK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user_equipo',
            name='equipo_FK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.equipo'),
        ),
        migrations.AlterField(
            model_name='user_equipo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]