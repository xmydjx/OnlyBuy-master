"""onlybuy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from apps import memberapp

from extra_apps import xadmin
from extra_apps.xadmin.plugins import xversion
xversion.register_models()

from apps.cart.views import *
from django.views.static import serve
from onlybuy.settings import MEDIA_ROOT

from apps.memberapp.views import GoodsSerializer
from apps.memberapp.views_base import GoodsListViews
from rest_framework.documentation import include_docs_urls
from apps.memberapp.views import GoodsListViewset
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
#配置goods的url
router.register(r'goods',GoodsListViewset)
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^list/',GoodsListViews.as_view(),name='goods-list'),
    url(r'docs/',include_docs_urls(title='onlybuy')),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    url(r'^',include(router.urls)),


    url(r'^static/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^user/', include('apps.userinfo.urls')),
    url(r'^cart/', include('apps.cart.urls')),
    url(r'^memberapp/', include('apps.memberapp.urls')),
    url(r'^order/', include('apps.order.urls')),
    url(r'^pay/', include('apps.pay.urls')),
    url(r'^index', include('apps.index.urls')),
    # url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^index', TemplateView.as_view(template_name="index.html"), name="index-1"),
    url(r'^header', TemplateView.as_view(template_name="header.html"), name="header"),
    url(r'^footer', TemplateView.as_view(template_name="footer.html"), name="footer"),
    url(r'^addressAdmin', TemplateView.as_view(template_name="addressAdmin.html"), name="addressAdmin"),
    url(r'^cart.html', TemplateView.as_view(template_name="cart.html"), name="cart"),
    url(r'^login', TemplateView.as_view(template_name="login.html"), name="login"),
    url(r'^lookforward', TemplateView.as_view(template_name="lookforward.html"), name="lookforward"),
    url(r'^myCollect', TemplateView.as_view(template_name="myCollect.html"), name="myCollect"),
    url(r'^myOrder', TemplateView.as_view(template_name="myOrder.html"), name="myOrder"),
    url(r'^orderInfo', TemplateView.as_view(template_name="orderInfo.html"), name="orderInfo"),
    url(r'^orderConfirm', TemplateView.as_view(template_name="orderConfirm.html"), name="orderConfirm"),
    url(r'^pay_fail', TemplateView.as_view(template_name="pay_fail.html"), name="pay_fail"),
    url(r'^pay_success', TemplateView.as_view(template_name="pay_success.html"), name="pay_success"),
    url(r'^payment', TemplateView.as_view(template_name="payment.html"), name="payment"),
    url(r'^personage', TemplateView.as_view(template_name="personage.html"), name="personage"),
    url(r'^personal_password', TemplateView.as_view(template_name="personal_password.html"), name="personal_password"),
    url(r'^product_details', TemplateView.as_view(template_name="product_details.html"), name="product_details"),
    url(r'^product_list', TemplateView.as_view(template_name="product_list.html"), name="product_list"),
    url(r'^register', TemplateView.as_view(template_name="register.html"), name="register"),
    url(r'^search_list', TemplateView.as_view(template_name="search_list.html"), name="search_list"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.CSS_URL, document_root=settings.CSS_PATH)+static(settings.JS_URL, document_root=settings.JS_PATH)+static(settings.JQ_URL, document_root=settings.JQ_PATH)

handler404 = memberapp.views.page_not_found