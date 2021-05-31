"""dar_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from report import views as report_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', report_views.home, name='home'),
    path('create-dar/', report_views.create_dar, name='create-dar'),
    path('<int:pk>/update/', report_views.DARUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', report_views.DARDeleteView.as_view(), name='delete'),
    path('send-emails-confirm/', report_views.send_emails_confirm, name='send-emails-confirm'),
    path('send-emails/', report_views.send_emails, name='send-emails'),
    path('login/', LoginView.as_view(template_name='report/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='report/logout.html'), name='logout'),
    
    
]
