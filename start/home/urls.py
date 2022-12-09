from django.urls import path
from.import views
urlpatterns = [
    path('',views.index),
    path('check/',views.CreateStudent),
    path('print/',views.CreateEmployee),
    path('home',views.show),
    path('detail',views.table, name='home'),
    path('delete/<str:id>/', views.delete, name='delete'),
    path('update/<str:id>/', views.update, name='update'),
    path('updaterecord/<str:id>/', views.updaterecord, name='update'),
]
