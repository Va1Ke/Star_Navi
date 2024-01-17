import django_filters
from socialNetwork.models import Like


class LikeFilterSet(django_filters.FilterSet):
    date_from = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    date_to = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Like
        fields = ["date_from", "date_to"]
