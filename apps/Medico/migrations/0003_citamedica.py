# Generated by Django 2.2.23 on 2021-05-21 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Medico', '0002_auto_20210520_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='CitaMedica',
            fields=[
                ('run', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_paciente', models.TextField()),
                ('tipo_prevision', models.CharField(choices=[('Pasteles', 'Pasteles'), ('Postres', 'Postres'), ('Comidas', 'Comidas'), ('Bebestibles', 'Bebestibles')], max_length=50)),
                ('fecha_cita', models.DateTimeField(auto_now_add=True)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Medico.Medico')),
            ],
        ),
    ]