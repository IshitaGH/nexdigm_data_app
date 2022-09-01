from django.db import models
from django.urls import reverse
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

MONTH_CHOICES = (
    (1, "Jan"),
    (2, "Feb"),
    (3, "Mar"),
    (4, "Apr"),
    (5, "May"),
    (6, "Jun"),
    (7, "Jul"),
    (8, "Aug"),
    (9, "Sept"),
    (10, "Oct"),
    (11, "Nov"),
    (12, "Dec"),
)

FILE_TYPE_CHOICES = (
    ("Inventory", "Inventory"),
    ("Distributory Sales", "Distributory Sales")
)

CONSOLIDATION_TYPE_CHOICES = (
    ("Monthly", "Monthly"),
    ("Yearly", "Yearly")
)

class Post(models.Model):
    num1 = models.DecimalField(max_digits=5, decimal_places=2)
    num2 = models.DecimalField(max_digits=5, decimal_places=2)
    add = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    square = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    neg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    # date_posted = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    #the actual interface
    #remove the null=True and blank=True when ready
    Year = models.IntegerField(('year'), validators=[MinValueValidator(1900), MaxValueValidator(2022)], null=True, blank=True)
    Month = models.IntegerField(choices=MONTH_CHOICES, null=True, blank=True)
    File_Type = models.CharField(max_length=100, choices=FILE_TYPE_CHOICES, null=True, blank=True)
    Consolidation_Type = models.CharField(max_length=100, choices=CONSOLIDATION_TYPE_CHOICES, null=True, blank=True)
    Dealer_1 = models.BooleanField(null=True, blank=True)
    Dealer_2 = models.BooleanField(null=True, blank=True)
    Dealer_3 = models.BooleanField(null=True, blank=True)
    Dealer_4 = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f'{self.num1}, {self.num2}'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})