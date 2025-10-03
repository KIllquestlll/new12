from django.db import models
from django.contrib.auth.models import User

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


class Comment(models.Model):
    # Комментарии к посту

    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.TextField()
    img = models.ImageField('Изображение',upload_to='media/%d',null=True,blank=True)
    data = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True,related_name='comments')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'