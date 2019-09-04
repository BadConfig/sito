from django.urls import path
from . import views

urlpatterns = [
        path('',views.testing_page),
        path('candidate',views.candidate_create,name='candidate')
        ]
