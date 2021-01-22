"""Memo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from rest_framework.urlpatterns import format_suffix_patterns

from Memo import settings
from personal.views import (
    home_screen_view
)

from account.views import (
    registration_view,
    logout_view,
    login_view,
    update_account_view,
    must_authenticate_view
)

from blog.views import (
    create_blog_view
)

urlpatterns = [
    # MY APPS URLS
    path('admin/', admin.site.urls),
    path('memo_app/', include('memo_app.urls')),
    path('', home_screen_view, name='home'),
    path('register', registration_view, name='register'),
    path('logout', logout_view, name='logout'),
    path('login', login_view, name='login'),
    path('account', update_account_view, name='account'),
    path('blog', include('blog.urls', 'blog')),
    path('must_authenticate', must_authenticate_view, name='must_authenticate'),


    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),

    # REST FRAMEWORK URLS
    path('api/memo_app/', include('memo_app.api.urls', 'memo_api')),
    path('api/account/', include('account.api.urls', 'account_api')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
