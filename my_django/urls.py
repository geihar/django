from django.contrib import admin
from django.urls import path, include
from users import views as userViews
from django.contrib.auth import views as loginViews
from django.conf import settings      #убрать при деплоеgit
from django.conf.urls.static import static     #убрать при деплое

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', userViews.registration, name='reg'),
    path('profile/', userViews.profile, name='profile'),
    path('login/', loginViews.LoginView.as_view(template_name='users/user.html'), name='log'),
    path('exit/', loginViews.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
    path('', include('main_page.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  #убрать при деплое
