from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('album', views.AlbumViewSet)
router.register('essay', views.PostViewSet)
router.register('files', views.FileViewSet)

urlpatterns = [
    path('', include(router.urls))
]
