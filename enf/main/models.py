from django.db import models

# Create your models here.


class Post(models.Model):
    # Модель поста
    title = models.CharField('Заголовок',max_length=50)
    description = models.TextField('Описание')
    img = models.ImageField('Изображение',upload_to='media/%d',null=True,blank=True)
    data = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'