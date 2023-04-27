from django.urls import path
from django.views.generic import ListView
from .views import BlogDetailView, Bloglist, AboutPageView


urlpatterns = [
    path('post/<int:pk>/', Bloglist.as_view(), name='post_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', Bloglist.as_view(), name='home'),
]
