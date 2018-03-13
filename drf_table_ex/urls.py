
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

#from musics.views import MusicViewSet, musics
from risk.views import RiskViewSet, ResponsesViewSet, dashboard_2

from django.views.generic import TemplateView

import mptt_urls  #for breadcrumbs


#The following adds the API links
router = DefaultRouter()
router.register(r'risk', RiskViewSet)
router.register(r'responses', ResponsesViewSet)
#router.register(r'music', MusicViewSet)


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    #The following injects the slug (path) into the url for the breadcrumbs
    url(r'^risk/(?P<path>.*)', mptt_urls.view(model='risk.models.Risk', view='risk.views.risk', slug_field='slug'), {'extra': ''}, name='risk'),

#    url(r'^risk2/(?P<path>.*)', mptt_urls.view(model='risk.models.Risk', view='risk.views.risk2', slug_field='slug'), {'extra': ''}, name='risk2'),

    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^dashboard_2/', dashboard_2),

]
