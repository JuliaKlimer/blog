from django.db import models

class Post(models.Model):
    title = models.CharField('Title', max_length=50)
    post = models.TextField('Post')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.id}'