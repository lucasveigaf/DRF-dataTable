
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from musics.views import MusicViewSet, musics
from risk.views import RiskViewSet, risks

from django.views.generic import TemplateView

import mptt_urls  #for breadcrumbs

router = DefaultRouter()
router.register(r'music', MusicViewSet)
router.register(r'risk', RiskViewSet)



urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html')),

    url(r'^musics/', musics),
    url(r'^risks/', risks),   
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),

    #The following code injects the slug (path) into the url for the breadcrumbs
    url(r'^risk/(?P<path>.*)', mptt_urls.view(model='risk.models.Risk', view='risk.views.risk', slug_field='slug'), {'extra': ''}, name='risk'),


]
