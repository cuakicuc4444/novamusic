from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

# Redirect root URL to login or homepage depending on authentication
def root_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # hoặc trang chính bạn muốn
    return redirect('login')

urlpatterns = [
    path('', root_view, name='root'),

    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),

    path('', include('home.urls')),
    path('', include('album.urls')),
    path('', include('artist.urls')),
    path('', include('genre.urls')),
    path('', include('music.urls')),
    path('', include('user.urls')),
    path('api/', include('API.urls')),

    path('admin/', admin.site.urls),

    # Password reset URLs
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='user/reset_password.html'), 
         name='reset_password'),
    
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='user/reset_password_sent.html'), 
         name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/reset.html'), 
         name='password_reset_confirm'),
    
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='user/reset_password_complete.html'), 
         name='password_reset_complete'),
]

# Static + media files in development
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
