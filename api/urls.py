from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AuthorViewSet

router = DefaultRouter()

router.register(r'author', AuthorViewSet)
router.register(r'books', BookViewSet)


urlpatterns = [
    path('', include(router.urls)), 
]