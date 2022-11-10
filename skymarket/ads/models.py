from django.conf import settings
from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=100, null=False, verbose_name="Название товара")
    price = models.PositiveIntegerField(null=False, verbose_name="Цена товара")
    description = models.CharField(max_length=250, default=False, verbose_name="Описание товара")
    author = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Имя пользователя, создавшего объявление")
    create_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Время и дата создания объявления")

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ["-create_at"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=200, null=False, verbose_name="Текст отзыва")
    author = models.ForeignKey("users.User", on_delete=models.CASCADE, null=False, verbose_name="Имя пользователя, создавшего отзыв")
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, null=False, verbose_name="Описание товара")
    create_at = models.DateTimeField(auto_now_add=True, null=False, verbose_name="Время и дата создания отзыва")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["-create_at"]

    def __str__(self):
        return self.text
