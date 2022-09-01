from django.db import models
from django.urls import reverse
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

class Post(models.Model):
    num1 = models.DecimalField(max_digits=5, decimal_places=2)
    num2 = models.DecimalField(max_digits=5, decimal_places=2)
    add = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    square = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    neg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    #the actual interface
    #remove the null=True and blank=True when ready
    year = models.IntegerField(('year'), validators=[MinValueValidator(1900), MaxValueValidator(2022)], null=True, blank=True)

    # date_posted = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.num1}, {self.num2}'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})