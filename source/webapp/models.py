from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.


User = get_user_model()

CATEGORY_CHOICES = [('0', 'other'), ('1', 'smartphone'),  ('2', 'computers')]


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Product name')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Product description')
    category = models.CharField(max_length=30, default='0', null=False, blank=False, choices=CATEGORY_CHOICES,
                                verbose_name='Category')
    picture = models.ImageField(verbose_name="Picture", upload_to="pictures/", null=True, blank=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'products'
        verbose_name = 'product'
        verbose_name_plural = 'products'


class Review(models.Model):
    author = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE, verbose_name="Author")
    product = models.ForeignKey("webapp.Product", on_delete=models.CASCADE, related_name="Reviews")
    content = models.TextField(max_length=1500, null=False, blank=False, verbose_name="Content")
    rate = models.PositiveIntegerField(verbose_name='Rate', null=False, blank=False,
                                       validators=[MinValueValidator(1), MaxValueValidator(5)])
    moderated = models.BooleanField(default=False, verbose_name="Moderated")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated date")