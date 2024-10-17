from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from app01 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),
    path("login/", views.login),
    path("sign/", views.sign),
    path("get_random_code/", views.get_random_code),

    re_path("^api/", include('api.api_urls')),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

]
