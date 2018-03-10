
from django.db import models
from django.db.models import Q
from model_utils import Choices

ORDER_COLUMN_CHOICES = Choices(
    ('0', 'id'),
    ('1', 'title'),
    ('2', 'description'),
    ('3', 'last_modify_date'),
    ('4', 'created'),
)


# Create your models here.
class Risk(models.Model):
    title = models.TextField()  # blank=False
    description = models.TextField()  # blank=False
    last_modify_date = models.DateTimeField(auto_now=True, null=True)     # setting auto_now or auto_now_add to True will cause the field to have editable=False and blank=True set.
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):        
        return self.title

    class Meta:
        db_table = "risk"


def query_risk_by_args(**kwargs):
    draw = int(kwargs.get('draw', None)[0])
    length = int(kwargs.get('length', None)[0])
    start = int(kwargs.get('start', None)[0])
    search_value = kwargs.get('search[value]', None)[0]
    order_column = kwargs.get('order[0][column]', None)[0]
    order = kwargs.get('order[0][dir]', None)[0]

    order_column = ORDER_COLUMN_CHOICES[order_column]
    # django orm '-' -> desc
    if order == 'desc':
        order_column = '-' + order_column

    queryset = Risk.objects.all()
    total = queryset.count()

    if search_value:
        queryset = queryset.filter(Q(id__icontains=search_value) |
                                        Q(title__icontains=search_value) |
                                        Q(description__icontains=search_value) |
                                        Q(last_modify_date__icontains=search_value) |
                                        Q(created__icontains=search_value))

    count = queryset.count()
    queryset = queryset.order_by(order_column)[start:start + length]
    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }
