"""cafe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from core.views import core_v
from orders.views import order_v
from menu_items.views import menu_item_v
from tables.views import table_v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', core_v),
    path('order/', order_v),
    path('menu_item/', menu_item_v),
    path('table/', table_v),
]
