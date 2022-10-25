from django.urls import path
from base import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('alumnos/', views.alumnos, name='alumnos'),
    path('alumnos/<int:alumn_id>', views.notas, name='notas'),
    path('faq/', views.faq, name='faq'),
    path('about/', views.about, name='about')
]