from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import CategoryViewSet, SubCategoryViewSet, AuthorViewSet,NewsViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubCategoryViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'news', NewsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
