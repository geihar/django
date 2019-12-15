from django.contrib import admin
from django.urls import path, include
from users import views as userViews
# from django.contrib.auth import views as loginViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', userViews.registration, name='reg'),
    # path('login/', loginViews.LoginView.as_view(template_name='users/user.html'), name='log'),
    # path('exit/', loginViews.LogoutView(template_name='users/exit.html'), name='exit'),
    path('', include('main_page.urls')),
]
