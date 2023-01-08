from django.urls import path
from .views import Signup_view,Login_view,Logout_view

urlpatterns=[
    path('sg/',Signup_view.as_view(),name='signup_url'),
    path('lv/',Login_view.as_view(),name='login_url'),
    path('lov/',Logout_view.as_view(),name='logout_url')
]