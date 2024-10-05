from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='DocuTrack-API',
        default_version='v1',
        description='DocuTrack API - это безопасная и масштабируемая API для хранения, управления и обмена документами.',
        terms_of_service='https://policies.google.com/',
        contact=openapi.Contact(
            name='Bekastan',
            url='https://my-bio-hstf.vercel.app/',
            email='5ekastannasirov@gmail.com'
        ),
        license=openapi.License(
            name='MIT License',
            url='https://opensource.org/license/mit',
        )
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
    path('api/v1/auth/', include('apps.accounts.urls')),
    path('api/v1/contents/', include('apps.contents.urls')),
    path('graphenes/api/v1/', include('apps.graphenes.urls')),
    path('api/v1/base-auth/', include('rest_framework.urls')),
]
