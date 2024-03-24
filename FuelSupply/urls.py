"""FuelSupply URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


#for_500 page
from django.urls import path
from django.conf.urls import handler500
from main.views import server_error_view  # Correct import path

handler500 = 'main.views.server_error_view'




urlpatterns = [
    path("iftofk/", admin.site.urls),
    path("", include("authentication.urls")),
    path("", include("main.urls")),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = (
    "  MUDOFAA VAZIRLIGINI AVTOMOBILLARNI MASOFADAN BUYURTMA BERISH VA ULARNING   YOQILG'I TA'MINOTINI AMALGA OSHIRUVHI SAYTNING ADMIN QISMI"
)
admin.site.site_title = "FuelSupply Admin"
admin.site.index_title = "FuelSupply sayti boshqaruv paneliga Xush kelibsiz"
