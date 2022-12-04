from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static #new

from . import views

app_name="cards"
urlpatterns = [
    path("", views.index ,name="index"),
    path("perekspb", views.perekspb, name="perek_spb"),
    path("peterechkaspb", views.peterechkaspb, name="peterechka_spb"),
    path("brizspb", views.brizspb, name="briz_spb"),
    path("vkusterspb", views.vkusterspb, name="vkuster_spb"),
    path("plovdivspb", views.plovdivspb, name="plovdiv_spb"),
    path("rosneftspb", views.rosneftspb, name="rosneft_spb"),
    path("dixyspb", views.dixyspb, name="dixy_spb"),
    path("prismaspb", views.prismaspb, name="prisma_spb"),
    path("vernyispb", views.vernyispb, name="vernyi_spb"),
    path("magnitspb", views.magnitspb, name="magnit_spb"),
    path("lentaspb", views.lentaspb, name="lenta_spb"),
    path("auchanspb", views.auchanspb, name="auchan_spb"),
    path("okspb", views.okspb, name="ok_spb")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)