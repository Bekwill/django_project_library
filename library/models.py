from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    picture = models.ImageField(upload_to='author/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    release_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

