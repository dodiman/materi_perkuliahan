from django.contrib import admin
from django.urls import path, include

# for image
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapi/', include('myapi.urls')),
    path('register', views.register, name="register_index"),
    path('logout', views.logoutPage, name="logout_index"),
    path('login', views.loginPage, name="login_index"),
    path('', views.index, name="index"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
