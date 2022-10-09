import os

from django.db import models


class Type(models.Model):
    name = models.CharField('Тип акта', max_length=50, unique=True)

    def __str__(self):
        return self.name



class Material(models.Model):
    name = models.CharField('Материал', max_length=50, blank=True)
    passport = models.FileField('Файл паспорта материала', upload_to='files/passports/', default=None)

    @property
    def filename(self):
        return os.path.basename(self.passport.name)

    # def save(self, *args, **kwargs):
    #     self.name = self.filename
    #     return super(Material, self).save(*args, **kwargs)


    def __str__(self):
        return self.name




class Project(models.Model):
    name = models.CharField('Наименование проекта', max_length=50)
    template = models.FileField('Файл-шаблон', upload_to='files/templates/')
    result_file = models.FileField('Итоговый архив', default=None)

    def __str__(self):
        return self.name


class Act(models.Model):
    act_type = models.ForeignKey(Type, verbose_name='Тип акта', on_delete=models.SET_NULL, null=True)
    number = models.CharField('Номер акта', max_length=50)
    materials = models.ManyToManyField(Material, verbose_name='Материалы', related_name='materials', blank=True)
    works = models.CharField('Проведенные работы', max_length=1000)
    order_number = models.PositiveSmallIntegerField('Порядковый номер акта в проекте')
    project = models.ForeignKey(Project, verbose_name='Проект', on_delete=models.CASCADE, related_name='acts', null=True)
    date_start = models.CharField('Дата начала работ', max_length=50, blank=True)
    date_end = models.CharField('Дата конца работ', max_length=50, blank=True)

    def __str__(self):
        return f'Акт №{self.order_number} {self.act_type}'
