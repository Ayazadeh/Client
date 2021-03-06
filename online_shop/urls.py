from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from online_shop import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('accounts/', include('customer.urls')),
                  path('', include('home.urls')),
                  path('order/', include('order.urls')),
                  path('product/', include('product.urls')),
                  path('#contact_us/', include('contact_us.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "online_shop.views.page_not_found_view"
