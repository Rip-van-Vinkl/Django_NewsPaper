from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.IntegerField(default=0)

#   def update_rating(self):


class Category(models.Model):
    
    category = models.CharField(max_length=40, unique=True)


class Post(models.Model):
    
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')

    news = 'NW'
    articles = 'AR'

    TYPE = [
        (news, 'news'),
        (articles, 'articles'),

    ]

    post_type = models.CharField(max_length=2, choices=TYPE)

    post_datetime = models.DateTimeField(auto_now_add=True)
    post_title = models.CharField(max_length=255)
    post_text = models.TextField()
    post_rating = models.IntegerField(default=0.0)

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

#    def preview(self):
#        return str(self.post_text[0:124], '...')


class PostCategory(models.Model):
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    comment_text = models.TextField()
    comment_datetime = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()