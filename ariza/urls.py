
from django.urls import path
from .views import index
from .views import login_view


from .views import(
    ariza,
    arizalar,
    avtopark,
    haydovchi,
    texnik_korik,
    xizmat_boshiliqlar,
    yoqilgi,


)

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path("ariza", ariza, name="ariza"),
    path("arizalar", arizalar, name="arizalar"),
    path("avtopark", avtopark, name="avtopark"),
    path("haydovchi", haydovchi, name="haydovchi"),
    path("texnik_korik", texnik_korik, name="texnik_korik"),
    path("xizmat_boshiliqlar", xizmat_boshiliqlar, name="xizmat_boshiliqlar"),
    path("yoqilgi", yoqilgi, name="yoqilgi"),
    



    
]
