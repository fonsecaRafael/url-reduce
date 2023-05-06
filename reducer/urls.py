from django.contrib import admin
from django.urls import path

from reducer.shorter import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('<slug:slug>', views.redirecter),
    path('reports/<slug:slug>', views.reports),
]
