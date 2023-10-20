from django.urls import path, re_path
from . import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('<int:user_id>/profile/', views.profile, name='profile'),
    path('<int:user_id>/profile/update-profile/', views.profileImageUpdate, name='update-profile'),
    path('<int:user_id>/profile/change-password/', views.changePassword, name='change-password'),
    path('<int:user_id>/admin-profile/', views.adminProfile, name='admin-profile'),
    path('<int:user_id>/admin-profile/update-profile/', views.adminProfileImageUpdate, name='admin-update-profile'),
    path('<int:user_id>/admin-profile/change-password/', views.adminChangePassword, name='admin-change-password'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)