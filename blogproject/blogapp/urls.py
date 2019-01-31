

from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index')	,
	path('try/', views.try_page, name='try'),
	path('blog-post/<int:pk>/', views.blog_post_view, name='blog-post'),
	path('blog-post/<int:pk>/home', views.blog_post_view, name='blog-post-eye'),
	path('about/',views.blog_about_page, name='about'),
	path('category/', views.category_view, name='category'),
	path('contact/', views.contact_page, name='contact'),
	path('write-for-us/', views.write_for_us, name='write4us'),
	path('write-for-us/let_start/sign', views.signin_page, name='signin'),
	path('eye/<int:pk>/', views.eye_catcher_post_view, name='eye'),
	# path('write-for-us/let_start/login/', views.login_page, name='login'),
]
