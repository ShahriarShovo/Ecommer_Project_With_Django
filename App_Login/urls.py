from django.urls import path
from App_Login import views


app_name="App_Login"

urlpatterns = [

    path('singup/', views.signup_user, name='singup'),
    path('login/', views.signin_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.user_profile , name='profile'),    
]
