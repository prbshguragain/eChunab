from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name="landing_page"),
    path('dashboard/', include('dashboard.urls')),
    path('accounts/', include('accounts.urls')),
]


urlpatterns += staticfiles_urlpatterns()
