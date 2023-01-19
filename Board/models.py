from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    title = models.CharField(max_length=100, unique=True)
    content = RichTextUploadingField()
    image = models.ImageField(default=0, null=True)
    pub_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.id}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=255, verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False, verbose_name='Принято')

    def __str__(self):
        return f'{self.text}'

    def is_accepted(self):
        return self.accepted