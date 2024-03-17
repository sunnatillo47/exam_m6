from django.shortcuts import render
from .models import Languages, Freamworks
# Create your views here.

def lan_fw(request):

    languages = Languages.objects.all()
    freamworks = Freamworks.objects.all()
    fw_list = []
    for n in freamworks:
        fw_list.append(n)
    return render(request, 'language.html', context={'languages': languages, 'freamworks':fw_list})

def lan_info(request, pk):

    info = Languages.objects.get(id=pk)

    return render(request, 'lan_info.html', context={'info': info})

def fw_info(request, pk):

    info = Freamworks.objects.get(id=pk)

    return render(request, 'fw_info.html', context={'info': info})