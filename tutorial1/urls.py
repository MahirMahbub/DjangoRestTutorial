"""tutorial1 URL Configuration

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
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework import routers

from quickstart import views as demo_views

# router = routers.DefaultRouter()
# router.register(r'users', demo_views.UserViewSet)
# router.register(r'groups', demo_views.GroupViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('', include('quickstart.urls')),
    path('', include('snippets.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # path(
    #     "docs/",
    #     SpectacularSwaggerView.as_view(
    #         template_name="swagger-ui.html", url_name="schema"
    #     ),
    #     name="swagger-ui",
    # ),
    # path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # # Optional UI:
    # path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]
