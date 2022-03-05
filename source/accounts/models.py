from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name="profile", verbose_name="профиль",
                                on_delete=models.CASCADE)
    about_info = models.TextField(max_length=300, null=True, blank=True, verbose_name="О себе")

    def __str__(self):
        return f"{self.user.username}'s Profile"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
