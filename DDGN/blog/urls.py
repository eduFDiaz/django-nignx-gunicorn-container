from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/category/<slug:category_slug>/', views.post_list_by_category, name='post__by_category'),
]
