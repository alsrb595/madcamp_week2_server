"""
URL configuration for madcamp_week2 project.

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

"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('myapp/', include('myapp.urls')),
    path('admin/', admin.site.urls), 
]

# url을 받아 파싱을 하고 path 별로 각기 다른 앱으로 분기가 되는 것, ~/myapp/ 경로로 요청이 들어오면 myapp으로 가서 동작하게 됨
"""

from django.contrib import admin #기본 관리자 인터페이스 사용하기 위한 모듈
from django.urls import path, include, re_path #url경로 설정 및 정규 표현식이 가능해짐
from django.conf import settings # setting 객체를 가져옴 setting.py에 접근이 가능
from rest_framework.permissions import AllowAny #모든 사용자가 접근이 가능하도록 
from drf_yasg import openapi # OpenAPI를 사양을 사용하여 API 문서를 생성하는데 사용
from drf_yasg.views import get_schema_view #OpenAPI 스키마 보기를 생성하는 함수임
from drf_yasg.generators import OpenAPISchemaGenerator #OpenAPI 스키마 생성기를 정의하는 classdla
from django.conf.urls.static import static
import oauthlib
import requests_oauthlib

schema_view = get_schema_view(
    openapi.Info(
        title="Your API Title",
        default_version='v1',
        description="API description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourdomain.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('users/', include('myapp.urls'), name='users'),
    path('community/', include('community.urls')),
    path('my_question/', include('user_questions.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     class BothHttpAndHttpSchemaGenerator(OpenAPIschemaGenerator): # 괄호 안의 클래스를 상속 받는 것임
#         def get_schema(self, request = None, public = False):
#             schema = super().get_schema(request, public)
#             schema.schemes = ["http", "https"] # 스키마의 속성 정의
#             return schema
        
#     schema_view = get_schema_view(
#         openapi.Info(
#             title = "Open API Swagger Test",
#             default_version = 'v1',
#             description = "시스템 API Description",
#         ),
#         public = True,
#         generator_class = BothHttpAndHttpSchemaGenerator,
#         permission_classes = (AllowAny,),
#     )

#     urlpatterns += [
#         re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout = 0), name = 'schema-json'),
#         re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name = 'schema-swagger-ui'),
#         re_path(r'^redoc/$',schema_view.with_ui('redoc', cache_timeout = 0), name = 'scheam-redoc'),
#     ]
