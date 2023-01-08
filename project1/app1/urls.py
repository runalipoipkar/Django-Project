from django.urls import path
from .views import Add_view,Update_view,Delete_view,Show_view


urlpatterns=[
    path('ad/',Add_view.as_view(),name='add_url'),
    path('sv/',Show_view.as_view(),name='show_url'),
    path('up/<int:pk>/',Update_view.as_view(),name='update_url'),
    path('dl/<int:pk>/',Delete_view.as_view(),name='delete_url')


]