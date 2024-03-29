"""ebury URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from trades.api import TradeListAPI, TradeDetailAPI
from trades.views import HomeView, DetailView, CreateView, DeleteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Trades URLs
    url(r'^$', HomeView.as_view(), name='trades_home'),
    url(r'^trades/(?P<pk>TR[A-Z0-9]+)$', DetailView.as_view(), name='trade_detail'),
    url(r'^trades/new$', CreateView.as_view(), name='new_trade'),
    url(r'^trades/delete/(?P<pk>TR[A-Z0-9]+)$', DeleteView.as_view(), name='delete_trade'),

    # Trades API URLs
    url(r'^api/1.0/trades/$', TradeListAPI.as_view(), name='trade_list_api'),
    url(r'^api/1.0/trades/(?P<pk>TR[A-Z0-9]+)$', TradeDetailAPI.as_view(), name='trade_detail_api'),
]
