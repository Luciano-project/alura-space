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

    return render(request, "gallery/index.html",{"cards":fotografias})

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


@login_required(login_url='login')
def editar_imagem(request, fotografia_id):

    fotografia = Fotografia.objects.get(id=fotografia_id)
    #fotos_autorizadas = foto.filter(usuario=request.username)
    form = FotografiaForms(request.POST or None, instance=fotografia)

    if request.method=="POST":
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, "Fotografia editada com sucesso!")
            return redirect("index")
        
    return render(request, "gallery/editar_imagem.html", {"form":form, "fotografia_id": fotografia_id})
    

@login_required(login_url='login')
def deletar_imagem(request, fotografia_id): 
    fotografia = Fotografia.objects.get(id=fotografia_id)
    fotografia.delete()
    messages.success(request, "Fotografia deletada com sucesso!")
    return redirect('index')

def filtro(request, categoria):
    fotografia = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True, categoria=categoria)
    return render(request, "gallery/index.html", {"cards":fotografia})
    