# Generated by Django 4.2.6 on 2023-10-31 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myrecipe', '0002_alter_recipe_steps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to='media/images/', verbose_name='Фото блюда'),
        ),
    ]
