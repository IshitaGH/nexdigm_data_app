from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from users.models import Profile

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
    ("Daily", "Daily"),
    ("Monthly", "Monthly")
)

# update these with the regions needed
REGION_CHOICES = (
    ("A", "A"),
    ("B", "B"),
)

# define the Post model that takes the meta-information
class Post(models.Model):
    # information collected/stored in order to run dummy scripts
    # during actual deployment, delete these from the class
    num1 = models.DecimalField(max_digits=5, decimal_places=2)
    num2 = models.DecimalField(max_digits=5, decimal_places=2)
    add = models.DecimalField(max_digits=500, decimal_places=2, null=True, blank=True)
    square = models.DecimalField(max_digits=500, decimal_places=2, null=True, blank=True)
    neg = models.DecimalField(max_digits=500, decimal_places=2, null=True, blank=True)

    #the actual model to be used in deployment
    #remove the null=True and blank=True then (it is there now so the dummy scripts may be run without filling out this information)
    Year = models.IntegerField(('year'), validators=[MinValueValidator(1900), MaxValueValidator(2022)], null=True, blank=True)
    Month = models.IntegerField(choices=MONTH_CHOICES, null=True, blank=True)
    File_Type = models.CharField(max_length=100, choices=FILE_TYPE_CHOICES, null=True, blank=True)
    Consolidation_Type = models.CharField(max_length=100, choices=CONSOLIDATION_TYPE_CHOICES, null=True, blank=True)
    # do NOT remove null=True, blank=True from author as the form will have trouble saving
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.num1}, {self.num2}'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

# define the data class that is used for the data records in the master data pages
class Data(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Distributor = models.IntegerField()
    Region = models.CharField(max_length=100, choices=REGION_CHOICES)
    Name = models.CharField(max_length=100)
    Selection = models.BooleanField()
    Currency = models.CharField(max_length=100)
    Product = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name