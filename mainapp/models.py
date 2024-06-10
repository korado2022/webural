# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


class Category(models.Model):
    """
    Модель категории товара содержит в себе поля:
    name - название категории
    url_img - ссылка на изображение категории
    slug - ссылка на категорию
    """

    name = models.CharField(max_length=255, unique=True)
    url_img = models.TextField(blank=True)
    slug = models.SlugField(max_length=128, unique=True)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def get_absolute_url(self):
        return reverse("mainapp:catalog", args=[self.slug])


class Group(models.Model):
    """
    Модель группы товара содержит в себе поля:
    name - название группы
    category - категория группы
    url_img - ссылка на изображение группы
    text - подробное описание группы
    slug - ссылка на группу
    """

    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    url_img = models.TextField(blank=True)
    text = RichTextField(blank=True)
    slug = models.SlugField(max_length=128, unique=True)



    def __str__(self):
        return f'{self.name} | {self.category}'

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def get_absolute_url(self):
        return reverse("mainapp:group", args=[self.slug])


class Subgroup(models.Model):
    """
    Модель подгруппы товара содержит в себе поля:
    name - название подгруппы
    group - группа подгруппы
    url_img - ссылка на изображение подгруппы
    text - подробное описание подгруппы
    slug - ссылка на подгруппу
    """

    name = models.CharField(max_length=255, unique=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="group")
    url_img = models.TextField(blank=True)
    text = RichTextField(blank=True)
    slug = models.SlugField(max_length=128, unique=True)



    def __str__(self):
        return f'{self.name} | {self.group}'

    class Meta:
        verbose_name = "Подгруппа"
        verbose_name_plural = "Подгруппы"

    def get_absolute_url(self):
        return reverse("mainapp:subgroup", args=[self.slug])




class Product(models.Model):
    """
    Модель товара содержит в себе поля:
    name - название товара
    description - краткое описание товара
    substance - вещество материала
    symbol - условное обозначение
    subgroup - подгруппа товара
    url_img - ссылка на изображение товара
    url_schema - ссылка на изображение схемы товара
    text - подробное описание товара
    slug - уникальный идентификатор товара, который используется в url
    """

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    substance = RichTextField(blank=True)
    symbol = RichTextField(blank=True)
    subgroup = models.ForeignKey(Subgroup, on_delete=models.CASCADE, related_name="subgroup")
    url_img = models.TextField(blank=True)
    url_schema = models.TextField(blank=True)
    text = RichTextField(blank=True)
    slug = models.SlugField(max_length=128, unique=True)

    def __str__(self):
        return f'{self.name} | {self.subgroup}'

    class Meta:
        verbose_name = "Изделие"
        verbose_name_plural = "Изделия"



# class Basket(models.Model):
#     """
#     Модель корзины, которая ссылается на товар.
#     Имеет поле is_send, которое отвечает за отправку заявки.
#     Может быть только одна запись на товар в корзине.
#     """
#
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product")
#     quantity = models.PositiveIntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     is_send = models.BooleanField(default=False)
#
#
#     def __str__(self):
#         return f"" f"{self.product.name}"
#
