from django.conf.urls.static import static

import ads.views
from django.contrib import admin
from django.urls import path, include

from avito import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ads.views.Index.as_view()),
    path('ads/', include('ads.urls.ads_urls')),
    path('cats/', include('ads.urls.categories_urls')),
    path('users/', include('users.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
