from django.shortcuts import render

from .models import *

# Create your views here.

def index(request):
    return render(request, "cards/index.html", {
        "shops": shops_SPB.objects.all(),
        "supermarkets": supermarkets_SPB.objects.all()
    })

def perekspb(request):
    return render(request, "cards/perek_spb.html", {
        "names": perek_spb.objects.all()
    })

def peterechkaspb(request):
    return render(request, "cards/peterechka_spb.html", {
        "shops": shops_SPB.objects.all(),
        "names": peterechka_spb.objects.all()
    })

def brizspb(request):
    return render(request, "cards/briz_spb.html", {
        "names": briz_spb.objects.all()
    })

def vkusterspb(request):
    return render(request, "cards/vkuster_spb.html", {
        "names": vkuster_spb.objects.all()
    })

def plovdivspb(request):
    return render(request, "cards/plovdiv_spb.html", {
        "names": plovdiv_spb.objects.all()
    })

def rosneftspb(request):
    return render(request, "cards/rosneft_spb.html", {
        "names": rosneft_spb.objects.all()
    })

def dixyspb(request):
    return render(request, "cards/dixy_spb.html", {
        "names": dixy_spb.objects.all()
    })

def prismaspb(request):
    return render(request, "cards/prisma_spb.html", {
        "names": prisma_spb.objects.all()
    })

def vernyispb(request):
    return render(request, "cards/vernyi_spb.html", {
        "names": vernyi_spb.objects.all()
    })

def magnitspb(request):
    return render(request, "cards/magnit_spb.html", {
        "names": magnit_spb.objects.all()
    })

def lentaspb(request):
    return render(request, "cards/lenta_spb.html", {
        "names": lenta_spb.objects.all()
    })

def auchanspb(request):
    return render(request, "cards/auchan_spb.html", {
        "names": auchan_spb.objects.all()
    })

def okspb(request):
    return render(request, "cards/ok_spb.html", {
        "names": ok_spb.objects.all()
    })