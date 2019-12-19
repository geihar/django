from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowNewsView.as_view(), name='main_page'),
    path('user/<str:username>/', views.ShowUserNews.as_view(), name='user_all_news'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='full_news'),
    path('news/<int:pk>/update/', views.UpdateNewsView.as_view(), name='update_news'),
    path('news/add/', views.CreateNewsView.as_view(), name='add_news'),
    path('news/<int:pk>/delete/', views.DeleteNewsView.as_view(), name='delete_news'),
    path('news/', views.news, name='news'),
]
