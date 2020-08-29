from django.urls import path, include
from .views import codeit, IDEViewSet
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'codes', views.IDEViewSet)

urlpatterns = [
    # path('', views.index, name='index'),
    path('codeit/', views.codeit, name='codeit'),
    path('run/', views.codeRun, name='run'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
