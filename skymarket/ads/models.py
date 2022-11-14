from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

User = get_user_model()


class Ad(models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(1)], verbose_name="Название")
    price = models.IntegerField(validators=[MinValueValidator(0)], verbose_name="Цена")
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name="Описание")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True, verbose_name="Картинка")

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(verbose_name="Текст", max_length=1000, validators=[MinLengthValidator(1)])
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name="Объявление")
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["-created_at"]

    def __str__(self):
        return self.text
