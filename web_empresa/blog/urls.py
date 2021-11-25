from django.urls import path
from .import views 

urlpatterns = [
    path('',views.blog, name = 'blog'),
    #el segundo parametro de la url por defecto se maneja como cadena de texto
    #poniendo int: antes del nombre de la variable forzamos a que se cambie el tipo de 
    #de la variable a entero
    path('category/<int:category_id>/', views.category, name='category')
]
