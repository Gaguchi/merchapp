from django.shortcuts import render

from .models import product

# Create your views here.

def index(request):
    return render(request, "cards/index.html", {
        "products": product.objects.all()
    })