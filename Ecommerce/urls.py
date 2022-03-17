
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('App_Login.urls')),
    path('home/', include('App_Shop.urls')),
    path('Shop/', include('App_Order.urls')),
    path('', views.index , name='index'),
    path('payment/', include('App_payment.urls')),
    path('search/', views.search_product, name='search'),
    
    

]


urlpatterns+= staticfiles_urlpatterns()
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)