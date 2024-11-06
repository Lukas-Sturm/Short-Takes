from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views, settings

urlpatterns = [
    path('', views.index, name='index'),
    path('takes/', include('takes.urls')),
    path('userprofile/', include('userprofile.urls')),
    path('search/', include('search.urls')),

    # Redirect to Builtin Login and Logout
    path('accounts/login/',
         auth_views.LoginView.as_view(template_name='auth/short-takes-login.html'), name='login'),
    path('accounts/logout/',
         auth_views.LogoutView.as_view(template_name='auth/short-takes-logout.html'), name='logout'),
    path('accounts/register/', views.register, name='register'),

    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
