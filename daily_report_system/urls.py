from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from employees.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('employees/', include('employees.urls')),
#    path('/', include('accounts.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
