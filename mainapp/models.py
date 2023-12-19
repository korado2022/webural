from django.db import models

# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    """
    Модель категории товара
    содержит в себе поля:
    name - название категории
    description - краткое описание категории
    url_img - ссылка на изображение категории
    """

    name = models.CharField(max_length=255, unique=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    """
    Модель товара
    Содержит в себе поля:
    name - название товара
    description - краткое описание товара
    substance - вещество материала
    symbol - условное обозначение
    category - категория товара
    url_img - ссылка на изображение товара
    url_schema - ссылка на изображение схемы товара
    slug - уникальный идентификатор товара, который используется в url
    """

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    substance = RichTextField(blank=True)
    symbol = RichTextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    url_img = models.TextField(blank=True)
    url_schema = models.TextField(blank=True)
    slug = models.SlugField(max_length=128, unique=True)


class Basket(models.Model):
    """
    Модель корзины, которая ссылается на товар.
    Имеет поле is_send, которое отвечает за отправку заявки.
    Может быть только одна запись на товар в корзине.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product")
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_send = models.BooleanField(default=False)


    def __str__(self):
        return f"" f"{self.product.name}"

