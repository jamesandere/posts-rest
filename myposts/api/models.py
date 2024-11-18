from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "authors"

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=200) 

    class Meta:
        db_table = "posts"

    def __str__(self):
        return self.title 