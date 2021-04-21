from django.urls import path
from . import views
from django.contrib import admin

admin.site.site_header = 'iDealer'
admin.site.site_title = "Welcome to iDealer's dashboard" 


urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('main', views.main, name='main'),
    path('registration', views.registration, name='registration'),
    path('create_user', views.register, name='register'),
    path('create_add', views.create_add),
    path('delete/<int:add_id>', views.delete_add),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

]
