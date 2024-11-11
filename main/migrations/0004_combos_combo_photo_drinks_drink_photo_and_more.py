# Generated by Django 5.1.2 on 2024-11-08 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_drinks_snacks_remove_ingredients_ingredient_point_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='combos',
            name='combo_photo',
            field=models.ImageField(null=True, upload_to='combos/', verbose_name='Иконка'),
        ),
        migrations.AddField(
            model_name='drinks',
            name='drink_photo',
            field=models.ImageField(null=True, upload_to='drinks/', verbose_name='Иконка'),
        ),
        migrations.AddField(
            model_name='snacks',
            name='snack_photo',
            field=models.ImageField(null=True, upload_to='snacks/', verbose_name='Иконка'),
        ),
    ]
