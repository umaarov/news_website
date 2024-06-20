from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="news/photos/", null=True, blank=True)

    def __str__(self):
        return self.title
