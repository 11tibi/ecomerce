from django.urls import path
from .views import Login, Register, Logout, Dashboard, UploadProfileImg
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('upload-profile-img/', UploadProfileImg.as_view(), name='upload_profile'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
