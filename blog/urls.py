from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('blog/<int:num>/', views.single_post, name='single_post')
]
