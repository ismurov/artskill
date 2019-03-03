from django.urls import path

from . import views

app_name = 'test'

urlpatterns = [
    path('', views.TestPage.as_view(), name='test'),
    path('1/', views.CategoryPage.as_view(), name='category'),
]