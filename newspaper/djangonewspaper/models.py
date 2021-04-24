from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    
    author = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Имя автора')
    author_rating = models.IntegerField(default=0, verbose_name='Рейтинг автора')
    
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
    
    def __str__(self):
        return self.author


    def update_rating(self):

        author_posts = Post.objects.filter(author = self.id)

        author_posts_sum_rating = 0
        for post in author_posts:
            author_posts_sum_rating += post.post_rating * 3

        author_comments_sum_rating = 0
        for сomments in Comment.objects.filter(user=self.author):
            author_comments_sum_rating += comments.comment_rating

        author_posts_comments_sum_rating = 0
        for comments in Comment.objects.filter(post=author_posts):
            author_posts_comments_sum_rating += comments.comment_rating

        self.author_rating = author_posts_sum_rating + author_comments_sum_rating + author_posts_comments_sum_rating
        self.save()

class Category(models.Model):
    
    category = models.CharField(max_length=40, unique=True, default='...')


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