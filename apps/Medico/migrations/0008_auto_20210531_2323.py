# Generated by Django 3.1.1 on 2021-06-01 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medico', '0007_auto_20210531_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citamedica',
            name='email',
            field=models.EmailField(blank=True, max_length=70, null=True),
        ),
    ]
