from django.urls import path
from App_Shop import views

app_name="App_Shop"

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('details/<pk>/', views.Product_Details.as_view(), name='details'),
    path('category/', views.Category.as_view(), name='category'),
    path('showCategoryWise/<pk>/', views.show_Category_Wise, name='showCategoryWise'),
    
   

]
