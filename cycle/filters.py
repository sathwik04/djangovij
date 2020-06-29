import django_filters

from.models import *
class Productfilter(django_filters.FilterSet):
    class Meta:
        model=Product
        fields='__all__'
class Orderfilter(django_filters.FilterSet):
    class Meta:
        model=Order
        fields='__all__'


