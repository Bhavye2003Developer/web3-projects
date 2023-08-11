from django.urls import path
from . import views

urlpatterns = [
    path('', views.transfer, name='home'),
    path('key', views.key, name='key'),
    path('createUser', views.createUser, name='createUser'),
    path('validate/<int:userID>', views.validate, name='validate'),
]
