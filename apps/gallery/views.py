from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.gallery.models import Fotografia

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "O usuário não está logado")
        return redirect('login')
    fotografia = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request,"gallery/index.html",{"cards":fotografia})


def imagem(request, fotografia_id):
    if not request.user.is_authenticated:
        messages.error(request, "O usuário não está logado")
        return redirect('login')
    fotografia = get_object_or_404(Fotografia, pk=fotografia_id)
    return render(request, "gallery/imagem.html", {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "O usuário não está logado")
        return redirect('login')
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_de_busca = request.GET["buscar"]
        if nome_de_busca:
            fotografias = fotografias.filter(nome__icontains=nome_de_busca)

    return render(request, "gallery/buscar.html",{"cards":fotografias})