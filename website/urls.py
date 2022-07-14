from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
path('',views.home,name='home'),
path('list/',views.list,name='list'),
path('blog/',views.blog,name='blog'),
path('blog-detail/',views.blog_detail,name='blog_detail'),
path('about/',views.about,name='about'),
path('contact/',views.contact,name='contact'),  
path('detay-kisi/',views.detay_kisi_create,name='detay_kisi'),

path('register/', views.register_request, name='register'),
path('login/', views.login_request, name='login'),
path("logout", views.logout_request, name= "logout"),

path('blog-category-update/<int:id>/',views.blog_category_update,name='blog-category-update'),
path('blog-category-delete/',views.blog_category_delete,name='blog-category-delete'),
path('deleteBlog/',views.deleteBlog,name='deleteBlog'),



]
