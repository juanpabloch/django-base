from django.urls import path
from cms import views

urlpatterns = [
    path('', views.index, name='cms_index'),
]