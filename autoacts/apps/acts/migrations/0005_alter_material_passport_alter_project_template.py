# Generated by Django 4.1.1 on 2022-09-13 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acts', '0004_act_materials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='passport',
            field=models.FileField(upload_to='files/passports/', verbose_name='Файл паспорта материала'),
        ),
        migrations.AlterField(
            model_name='project',
            name='template',
            field=models.FileField(upload_to='files/templates/', verbose_name='Файл-шаблон'),
        ),
    ]