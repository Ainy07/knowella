from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)

    trending_score = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_score(self):
        score = (self.likes * 3) + (self.comments * 5) + (self.shares * 7)
        self.trending_score = score
        self.save()

    def __str__(self):
        return self.title