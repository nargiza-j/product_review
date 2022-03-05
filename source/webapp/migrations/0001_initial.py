# Generated by Django 4.0.3 on 2022-03-05 07:14

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Product name')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Product description')),
                ('category', models.CharField(choices=[('0', 'other'), ('1', 'smartphone'), ('2', 'computers')], default='0', max_length=30, verbose_name='Category')),
                ('picture', models.ImageField(null=True, upload_to='pictures/', verbose_name='Picture')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=1500, verbose_name='Content')),
                ('rate', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Rate')),
                ('moderated', models.BooleanField(default=False, verbose_name='Moderated')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reviews', to='webapp.product')),
            ],
        ),
    ]