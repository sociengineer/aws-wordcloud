from .models import Review
import django_filters


class ReviewFilter(django_filters.FilterSet):
    categories = django_filters.CharFilter(lookup_expr='icontains')
    city = django_filters.CharFilter(lookup_expr='icontains')
    country = django_filters.CharFilter(lookup_expr='icontains')
    name = django_filters.CharFilter(lookup_expr='icontains')
    date = django_filters.NumberFilter(field_name='date')
    rating = django_filters.NumberFilter(field_name='rating')
    tokens = django_filters.CharFilter(field_name='tokens')

    class Meta:
        model = Review
        fields = ['categories', 'city', 'country','name','date','rating', 'tokens']
