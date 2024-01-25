from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.gallery.models import Fotografia
from apps.gallery.forms import FotografiaForms

# Create your views here.
@login_required(login_url='login')
def index(request):

    fotografia = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request,"gallery/index.html",{"cards":fotografia})

@login_required(login_url='login')
def imagem(request, fotografia_id):

    fotografia = get_object_or_404(Fotografia, pk=fotografia_id)
    return render(request, "gallery/imagem.html", {"fotografia": fotografia})

@login_required(login_url='login')
def buscar(request):

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_de_busca = request.GET["buscar"]
        if nome_de_busca:
            fotografias = fotografias.filter(nome__icontains=nome_de_busca)

    return render(request, "gallery/buscar.html",{"cards":fotografias})

@login_required(login_url='login')
def nova_imagem(request):
    form = FotografiaForms()
    if request.method == "POST":
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Fotografia adicionada com sucesso!")
            return redirect("index")
    return render(request, "gallery/nova_imagem.html", {"form":form})

def editar_imagem(request): pass

def deletar_imagem(request): 
    if not request.user.is_authenticated:
        pass