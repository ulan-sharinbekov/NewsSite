from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField( max_length=255, verbose_name="заголовок")
    content = models.TextField(blank=True, verbose_name="Контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создание")
    update_at = models.DateTimeField(auto_now=True, verbose_name="дата изменения")
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name="картинки")
    is_publisher = models.BooleanField(default=True, verbose_name="публикация")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='категория', null=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering =['-created_at']

class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='заголовок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
