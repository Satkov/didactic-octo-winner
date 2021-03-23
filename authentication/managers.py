from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Пользовательская модель User, где уникальным идентификатором
    служит поле email
    """
    def create_user(self, email, username, **extra_fields):
        """
         Создаём и сохраняем пользователя по почте и паролю.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.save()
        return user

    def create_superuser(self, email, username, **extra_fields):
        """
        Создаём и сохраняем суперпользователя по почте и паролю.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, username, **extra_fields)