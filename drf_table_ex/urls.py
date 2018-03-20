
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from musics.views import MusicViewSet, musics
from risk.views import RiskViewSet, ResponsesViewSet, dashboard_2
from django.views.generic import TemplateView
import mptt_urls

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^risk/(?P<path>.*)', mptt_urls.view(model='risk.models.Risk', view='risk.views.risk', slug_field='slug'), {'extra': ''}, name='risk'),
    url(r'^country/(?P<path>.*)', mptt_urls.view(model='risk.models.Country', view='risk.views.country', slug_field='slug'), {'extra': ''}, name='country'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/risk/(?P<risk_slug>[\w+]+)', RiskViewSet.as_view({'get': 'list'})),
    url(r'^api/responses/(?P<response_slug>[\w+]+)', ResponsesViewSet.as_view({'get': 'list'})),
    url(r'^dashboard_2/', dashboard_2),
    url(r'^musics/', musics),

]
