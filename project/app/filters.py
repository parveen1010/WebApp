import django_filters
from django_filters import DateFilter,CharFilter
from .models import *


class CustomerFilter(django_filters.FilterSet):
	class Meta:
		model = Customer
		fields = '__all__'