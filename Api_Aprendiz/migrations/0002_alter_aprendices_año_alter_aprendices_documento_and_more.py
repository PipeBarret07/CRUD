# Generated by Django 4.2.4 on 2023-08-31 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api_Aprendiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aprendices',
            name='año',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='aprendices',
            name='documento',
            field=models.PositiveBigIntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='aprendices',
            name='numero_de_ficha',
            field=models.PositiveBigIntegerField(max_length=7),
        ),
    ]
