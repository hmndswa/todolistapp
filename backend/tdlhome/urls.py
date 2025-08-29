from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication
    path('accounts/login/',  auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),

    # Logout
    path('accounts/logout/', auth_views.LogoutView.as_view(
        next_page='login'
    ), name='logout'),

    # Signup
    path('accounts/signup/', accounts_views.signup, name='accounts_signup'),

    # Todo app
    path('', include('tdlapp.urls')),
]
