"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from Ghosty_API import views
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter(trailing_slash=False)

router.register(r'works', views.WorkViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'deceased', views.DeceasedViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
                  url(r'^api/', include(router.urls, namespace='api')),
                  url(r'^admin/', admin.site.urls),
                  url(r'^docs/', include('rest_framework_docs.urls')),
                  url(r'^api-token-auth/', obtain_jwt_token),
                  url(r'^api-token-refresh/', refresh_jwt_token),
                  url(r'^api-token-verify/', verify_jwt_token),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
