from django.db import models
from django.urls import reverse

# Create your models here.

# class num1(models.Model):
#     num1 = models.DecimalField(max_digits=5, decimal_places=2)

#     def __str__(self):
#         return f'num1: {self.num1}'

# class num2(models.Model):
#     num2 = models.DecimalField(max_digits=5, decimal_places=2)

#     def __str__(self):
#         return f'num1: {self.num2}'

class Post(models.Model):
    num1 = models.DecimalField(max_digits=5, decimal_places=2)
    num2 = models.DecimalField(max_digits=5, decimal_places=2)
    # date_posted = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.num1}'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})