# Generated by Django 4.1.3 on 2022-12-09 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dssProject', '0003_alter_maquina_tarea'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mantencion',
            fields=[
                ('id_mantencion', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('id_maquina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dssProject.maquina')),
            ],
        ),
    ]
