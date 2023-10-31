from django.contrib.auth.models import User
from django.db import models
from django.db import migrations


CATEGORY = (
        ('салаты и закуски', 'Салаты и закуски'),
        ('супы', 'Супы'),
        ('вторые блюда. мясо', 'Вторые блюда. Мясо'),
        ('вторые блюда. птица', 'Вторые блюда. Птица'),
        ('вторые блюда. рыба и морепродукты', 'Вторые блюда. Рыба и морепродукты'),
        ('гарниры и соусы', 'Гарниры и соусы'),
        ('хлеб и выпечка', 'Хлеб и выпечка'),
        ('десерты', 'Десерты'),
        ('напитки. алкоголь', 'Напитки. Алкоголь'),
        ('напитки. без алкоголя', 'Напитки. Без алкоголя')
)

class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=50, choices=CATEGORY)

class Recipe(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50)
    description = models.CharField(verbose_name='Описание', max_length=500)
    steps = models.CharField(verbose_name='Этапы приготовления', max_length=10000)
    cooking_time = models.IntegerField(verbose_name='Время приготовления, мин')
    image = models.ImageField(verbose_name='Фото блюда', upload_to='media/images/')
    create_at = models.DateTimeField(verbose_name='Время публикации', auto_now = True)


class CookingItem(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)


