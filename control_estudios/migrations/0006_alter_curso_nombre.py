# Generated by Django 4.2.3 on 2023-07-28 19:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_estudios', '0005_curso_profesor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='nombre',
            field=models.CharField(max_length=64, validators=[django.core.validators.RegexValidator('^[A-Za-z ]*$', 'Ingrese un nombre sin numeros.')]),
        ),
    ]
