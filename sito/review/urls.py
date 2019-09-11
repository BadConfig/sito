from django.urls import path
from . import views

urlpatterns = [
        path('user',views.create,name='create'),
        path('show',views.show),
        path('login',views.LogIn_view),
        path('signup',views.SignUp_view),
        ]
