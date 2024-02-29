from django.shortcuts import render
from .models import MyModel

# def index(request):
#     my_models = MyModel.objects.all()
#     return render(request, 'index.html', {'my_models': my_models})

# views.py

def login_view(request):
    return render(request, 'login.html')

def index(request):
    context = {}

    return render(request, "index.html", context=context)

def ariza(request):
    context = {}

    return render(request, "ariza.html", context=context)



def avtopark(request):
    context = {}

    return render(request, "avtopark.html", context=context)

def haydovchi(request):
    context = {}

    return render(request, "haydovchi.html", context=context)

def texnik_korik(request):
    context = {}

    return render(request, "texnik_korik.html", context=context)

def xizmat_boshiliqlar(request):
    context = {}

    return render(request, "xizmat_boshiliqlar.html", context=context)

def yoqilgi(request):
    context = {}

    return render(request, "yoqilgi.html", context=context)

def arizalar(request):
    context = {}

    return render(request, "arizalar.html", context=context)
