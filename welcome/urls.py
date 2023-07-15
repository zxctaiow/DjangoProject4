from . import views
from django.urls import path

app_name = 'welcome'

urlpatterns = [
    path('', views.IndexView.as_view(), name='main'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('news/add', views.NewsAdd.as_view(), name='create'),
    path('news/<int:pk>/detail', views.NewsDetail.as_view(), name='detail'),
    path('news/<int:pk>/delete', views.NewsDelete.as_view(), name='delete'),
]