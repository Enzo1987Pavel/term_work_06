from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from users.managers import UserManager, UserRoles
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100, validators=[MinLengthValidator(1)], verbose_name="Имя пользователя")
    last_name = models.CharField(max_length=100, validators=[MinLengthValidator(1)], verbose_name="Фамилия пользователя")
    phone = PhoneNumberField(validators=[MinLengthValidator(1)], verbose_name="Телефон для связи")
    email = models.EmailField(max_length=100, unique=True, validators=[MinLengthValidator(1)], verbose_name="Электронная почта пользователя")
    role = models.CharField(max_length=5, verbose_name="Роль пользователя", choices=UserRoles.choices, default=UserRoles.USER)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(verbose_name="Аватарка пользователя", null=True, blank=True)

    # эта константа определяет поле для логина пользователя
    USERNAME_FIELD = "email"

    # эта константа содержит список с полями, которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ["first_name", "last_name", "phone", "role"]

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
