import os
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator

from .routers import router
class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):

    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["https", "http"]
        # schema.basePath = os.path.join('/svec', 'ivms', 'reporting', 'api', 'v1')
        return schema


schema_view = get_schema_view(
    info=openapi.Info(
        title="IVMS API",
        default_version='v1',
        description="V1 API for IVMS"),
    public=True,
    generator_class=BothHttpAndHttpsSchemaGenerator, # Here
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[],
)


urlpatterns = [
    # ---------------
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # ---------------
    path('grappelli/', include('grappelli.urls')),
    # ---------------
    path('admin/', admin.site.urls),
    # ---------------
    path('api-auth/', include('rest_framework.urls')),
    # ---------------
    path('api/', include(router.urls)),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




# django admin tools dashboard
ADMIN_TOOLS_INDEX_DASHBOARD = 'ivms.dashboard.CustomIndexDashboard'
