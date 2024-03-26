from django.urls import path
from . import views 
from user import views as user_views

urlpatterns=[
    path('',user_views.register,name='register'),
    #path('profile',views.profile,name='profile'),
]    
