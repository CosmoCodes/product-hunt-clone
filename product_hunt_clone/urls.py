from django.contrib import admin
from django.urls import path,include
from products import views as prodViews
from accounts import views as accViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',prodViews.home,name='home'),
    path('accounts/',include('accounts.urls'),name='accounts'),
]
