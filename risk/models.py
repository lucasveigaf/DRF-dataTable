
from django.db import models
from django.db.models import Q
from model_utils import Choices
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey 

class Risk(MPTTModel):
    title            = models.CharField('Risk category name', max_length=200)
    parent           = TreeForeignKey('self', null=True, blank=True, verbose_name='parent category', related_name='riskcategories', on_delete=models.CASCADE)
    description      = models.TextField('Description', max_length=700)  
    slug             = models.SlugField(unique=True)
    last_modify_date = models.DateTimeField(auto_now=True, null=True)     # setting auto_now or auto_now_add to True will cause the field to have editable=False and blank=True set.
    created          = models.DateTimeField(auto_now_add=True, null=True)

    #Used by django-mptt-urls in making breadcrumbs
    def get_absolute_url(self):
        return reverse('risk', kwargs={'path': self.get_path()})

    def __str__(self):        
        return self.title

ORDER_COLUMN_CHOICES = Choices(
    ('0', 'id'),
    ('1', 'title'),
    ('2', 'last_modify_date'),
    ('3', 'created'),
    )

RESPONSES_CATEGORY = (  
    ('ACC', 'Accept'),    
    ('MIT', 'Mitigate'),
    ('INS', 'Insure'),
    ('HED', 'Hedge'),
)

class Responses(models.Model):
#    risk              = models.ForeignKey(Risk, null=True, blank=True, db_index=True, on_delete=models.CASCADE)
    risk              = TreeForeignKey(Risk, null=True, blank=True, db_index=True, on_delete=models.CASCADE)
    responsesCategory = models.CharField('Responses category', max_length=3, choices=RESPONSES_CATEGORY, default="ACC")
    description       = models.TextField('Description', max_length=300, default="Detailed description")
    last_modify_date  = models.DateTimeField(auto_now=True, null=True)     # setting auto_now or auto_now_add to True will cause the field to have editable=False and blank=True set.
    created           = models.DateTimeField(auto_now_add=True, null=True)
    deadlineDate      = models.DateField(auto_now_add=True, null=True)    

    def __str__(self):        
        return self.description
        
    class Meta:
        verbose_name_plural = 'Responses'


class Country(MPTTModel):
    title    = models.CharField('Country name', max_length=50)
    parent   = TreeForeignKey('self', null=True, blank=True, verbose_name='parent category', related_name='countries', on_delete=models.CASCADE)
    slug     = models.SlugField(unique=True, default='slug')
    
    def __str__(self):        
        return self.title

    def get_absolute_url(self):
        return reverse('country', kwargs={'path': self.get_path()})

    class Meta:
        verbose_name_plural = 'Countries'


