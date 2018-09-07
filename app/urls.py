"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
# from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework.documentation import include_docs_urls

from django.contrib import staticfiles
from django.urls import path
from app.settings import MEDIA_ROOT
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
import xadmin
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
import  DjangoUeditor
from  DjangoUeditor  import  urls as  DjangoUeditor_urls
from goods.views import GoodsListViewSet, CategoryViewset, HotSearchsViewset, BannerViewset, IndexCategoryViewset

from django.views.generic import TemplateView

#配置goods的url
router = DefaultRouter()
router.register(r'goods', GoodsListViewSet)
#配置category的url
router.register(r'categorys', CategoryViewset, base_name="categorys")
router.register(r'hotsearchs', HotSearchsViewset, base_name="hotsearchs")
#轮播图url
router.register(r'banners', BannerViewset, base_name="banners")
#首页商品系列数据
router.register(r'indexgoods', IndexCategoryViewset, base_name="indexgoods")
urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'docs/', include_docs_urls(title="亚坤")),
    path(r'xadmin/', xadmin.site.urls),
    # drf自带的token认证模式
    path(r'^api-token-auth/', views.obtain_auth_token),
    # url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    path(r'ueditor/', include('DjangoUeditor.urls')),
    path('', include(router.urls))


# url(r'^ueditor/', include(DjangoUeditor_urls))


]
urlpatterns += staticfiles_urlpatterns()