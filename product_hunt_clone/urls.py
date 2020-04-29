from django.contrib import admin
from django.urls import path,include
from products import views as prodViews
from accounts import views as accViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',prodViews.home,name='home'),
    path('accounts/',include('accounts.urls'),name='accounts'),
    path('products/',include('products.urls'),name='products'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
