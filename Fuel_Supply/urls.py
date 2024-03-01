from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ariza.urls')),
    path('accout/', include('accouts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# admin.site.site_header = (
#     "Yoqilg'i taminoti"
# )
# admin.site.site_title = "Yoqilg'i taminoti Admin"
# admin.site.index_title = "Yoqilg'i taminotining sayti boshqaruv paneliga Xush kelibsiz"
