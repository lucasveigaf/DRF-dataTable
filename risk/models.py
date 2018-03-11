
from django.db import models
from django.db.models import Q
from model_utils import Choices

from mptt.models import MPTTModel, TreeForeignKey 


# Hazard (mptt) ----------------------------------------


class Hazard(MPTTModel):
    title             = models.CharField('Hazard category name', max_length=200)
    parent            = TreeForeignKey('self', null=True, blank=True, verbose_name='parent category', related_name='hazardcategories', on_delete=models.CASCADE)
    description       = models.TextField('Description', max_length=700)  
    slug              = models.SlugField(unique=True)
    last_modify_date  = models.DateTimeField(auto_now=True, null=True)     # setting auto_now or auto_now_add to True will cause the field to have editable=False and blank=True set.
    created           = models.DateTimeField(auto_now_add=True, null=True)

    # Required by django-serialization-recursive  
    def children(self):
        return Hazard.objects.filter(parent=self)
    
    #Used by django-mptt-urls in making breadcrumbs
    def get_absolute_url(self):
        return reverse('hazard', kwargs={'path': self.get_path()})

    def __str__(self):        
        return self.title

ORDER_COLUMN_CHOICES = Choices(
    ('0', 'id'),
    ('1', 'title'),
    ('2', 'last_modify_date'),
    ('3', 'created'),
)

# Hazard datatable
def query_hazard_by_args(**kwargs):                
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

    queryset = Hazard.objects.all()      #modify the queryset here
    total = queryset.count()

    if search_value:
        queryset = queryset.filter(Q(id__icontains=search_value) |
                                        Q(title__icontains=search_value) |
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



# Risk (non mptt) ----------------------------------------


class Risk(models.Model):
    title = models.TextField()  # blank=False
    description = models.TextField()  # blank=False
    last_modify_date = models.DateTimeField(auto_now=True, null=True)     # setting auto_now or auto_now_add to True will cause the field to have editable=False and blank=True set.
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):        
        return self.title

    class Meta:
        db_table = "risk"

ORDER_COLUMN_CHOICES = Choices(
    ('0', 'id'),
    ('1', 'title'),
    ('2', 'description'),
    ('3', 'last_modify_date'),
    ('4', 'created'),
)

# Risk datatable
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

    queryset = Risk.objects.all()      #modify the queryset here
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
