from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('user/', include('post.urls')),

]#+ static(settings.MEDIA_URL, PROJECT_root= settings.MEDIA_ROOT)

