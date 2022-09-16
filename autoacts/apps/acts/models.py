import os

from django.db import models


class Type(models.Model):
    name = models.CharField('Тип акта', max_length=50)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField('Материал', max_length=50)
    passport = models.FileField('Файл паспорта материала', upload_to='files/passports/')

    @property
    def filename(self):
        return os.path.basename(self.passport.name)

    def __str__(self):
        return self.name + self.filename


class Project(models.Model):
    name = models.CharField('Наименование проекта', max_length=50)
    template = models.FileField('Файл-шаблон', upload_to='files/templates/')
    result_file = models.FileField('Итоговый архив', default=None)

    def __str__(self):
        return self.name


class Act(models.Model):
    act_type = models.ForeignKey(Type, verbose_name='Тип акта', on_delete=models.CASCADE)
    number = models.CharField('Номер акта', max_length=50)
    materials = models.ManyToManyField(Material, verbose_name='Материалы', related_name='materials')
    works = models.CharField('Проведенные работы', max_length=500)
    order_number = models.PositiveSmallIntegerField('Порядковый номер акта в проекте')
    project = models.ForeignKey(Project, verbose_name='Проект', on_delete=models.CASCADE, related_name='acts', )

    def __str__(self):
        return f'Акт №{self.order_number} {self.act_type}'
