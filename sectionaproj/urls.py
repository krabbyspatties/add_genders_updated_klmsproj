from django.urls import path 
from . import views

urlpatterns = [
    path('genders', views.index_genders),
    path('genders/create', views.create_gender),
    path('genders_store', views.store_gender), 
    path('users', views.index_users)
]
