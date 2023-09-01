from django.db import models

# Create your models here.
class BookCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    authors = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    published_date = models.DateField()
    distribution_expense = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title