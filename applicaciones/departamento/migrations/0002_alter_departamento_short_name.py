# Generated by Django 4.0.6 on 2022-07-26 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='short_name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Nombre Corto'),
        ),
    ]
