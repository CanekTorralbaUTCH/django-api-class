from django.contrib import admin
from django.urls import path

#Static files config
from django.conf import settings
from django.conf.urls.static import static

from users.views import users as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', users_views.users, name='users'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
