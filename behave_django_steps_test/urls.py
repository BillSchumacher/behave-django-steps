"""
URL configuration for behave_django_steps_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path

from behave_django_steps_test.routers.drf import router as drf_router
from behave_django_steps_test.routers.dynamic import router as dynamic_router

urlpatterns = [
    path("dynamic/", include(dynamic_router.urls)),
    path("drf/", include(drf_router.urls)),
    path("admin/", admin.site.urls),
]
