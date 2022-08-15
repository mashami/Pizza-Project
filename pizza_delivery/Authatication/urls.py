import imp
from django.urls import path
from . import views
urlpatterns = [
    path('',views.HelloAuthAPIView.as_view()),
    path('signup/',views.UserAPIView.as_view(),name='Sign_up'),
    
]
