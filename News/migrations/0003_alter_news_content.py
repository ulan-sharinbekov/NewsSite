# Generated by Django 4.0.3 on 2022-03-11 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_category_alter_news_options_news_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(blank=True, verbose_name='Контент'),
        ),
    ]
