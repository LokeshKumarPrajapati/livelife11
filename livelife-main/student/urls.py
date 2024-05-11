from . import views
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='Student-Home'),
    re_path(r'.*home/$',views.index,name="index"),
    path('home/', views.index, name='index'),
    path('res', views.view_responses, name='Student-Home'),
    path('about/', views.about, name='Student-Home'),
    path('contact/', views.contact, name='Student-Home'),
    path('gallery/', views.gallery, name='Student-Home'),
    path('blog-grid/', views.blogs, name='Student-Home'),
    path('blog-left-sidebar/', views.blogs, name='Student-Home'),
    path('contact/', views.blogs, name='Student-Home'),
    path('certificate/', views.certificate, name='Student-Home'),
    path('rescue/', views.blogs, name='Student-Home'),
    path('events/', views.blogs, name='Student-Home'),
    

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)