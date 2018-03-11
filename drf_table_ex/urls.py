
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from musics.views import MusicViewSet, index
from risk.views import RiskViewSet, risks

router = DefaultRouter()
router.register(r'music', MusicViewSet)
router.register(r'risk', RiskViewSet)

urlpatterns = [
    url(r'^index/', index),
    url(r'^risks/', risks),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls))
]
