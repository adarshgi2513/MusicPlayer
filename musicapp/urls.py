from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('datas/', views.data_views, name='data_views'),
    path('searchbar/', views.searchbar, name='searchbar'),
    path('form/',views.form,name='form'),
    path('save/',views.save,name='save'),
    
     
    
       

]
