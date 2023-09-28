from django.contrib import admin
from django.urls import path
from app import views
from app.views import about, write_for_us, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('about', about, name='about'),
    path('write-for-us', write_for_us, name='write_for_us'),
    path('contact', contact, name='contact'),
    
]
