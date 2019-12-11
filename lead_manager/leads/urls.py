from rest_framework import routers
from .api import LeadViewSet


routers = routers.DefaultRouter()
routers.register('api/leads',LeadViewSet,'leads')

urlpatterns = routers.urls
