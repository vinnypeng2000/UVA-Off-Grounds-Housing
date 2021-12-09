from django.db.models import fields
from django.http.request import QueryDict
import django_filters
from django_filters import NumberFilter

from .models import *


class StyleFilter(django_filters.FilterSet):
    rent_max = NumberFilter(field_name = 'rent', lookup_expr = 'lt')
    
    class Meta:
        model = Style
        fields = '__all__'
        exclude = ['name', 'rent']

class HousingFilter(django_filters.FilterSet):

    class Meta:
        model = Housing
        fields = '__all__'
        exclude = [
            'name', 
            'address', 
            'date published', 
            'pub_date', 
            'admin_check',
            'lat',
            'long',
            'people_low',
            'people_up',
            'beds_low',
            'beds_up',
            'baths_low',
            'baths_up', 
            'image'
        ]