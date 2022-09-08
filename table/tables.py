import django_tables2 as tables
from .models import Data

class Currency_Master(tables.Table):
    class Meta:
        model = Data
        template_name = "django_tables2/bootstrap.html"
        fields = ("Distributor", "Region", "Name", "Selection", "Currency" )

class Product_Master(tables.Table):
    class Meta:
        model = Data
        template_name = "django_tables2/bootstrap.html"
        fields = ("Distributor", "Region", "Name", "Selection", "Product" )

class Distributor_Master(tables.Table):
    class Meta:
        model = Data
        template_name = "django_tables2/bootstrap.html"
        fields = ("Distributor", "Region", "Name", "Selection", "Distributor" )