# Generated by Django 3.1.7 on 2021-09-18 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0022_auto_20210918_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_equipo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='principal.profile'),
        ),
    ]
