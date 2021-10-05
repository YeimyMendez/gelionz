# Generated by Django 3.1.7 on 2021-09-15 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0011_auto_20210915_1016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_equipo',
            old_name='user_FK',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='user_FK',
        ),
        migrations.AlterField(
            model_name='evento',
            name='organizador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.profile'),
        ),
    ]
