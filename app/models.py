from django.core.validators import RegexValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_sub')

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True, validators=[RegexValidator('^\\+?1?\d{9,9}$',
                                                                                           message="Telefon raqami '999999999' formatida bo'lishi kerak. Maksimal 9 ta raqam.")])

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_news')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='subcategory_news')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='Author_news')
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
