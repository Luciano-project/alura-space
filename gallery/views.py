from django.shortcuts import render, get_object_or_404
from .models import Fotografia



# Create your views here.
def index(request):
    fotografia = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request,"gallery/index.html",{"cards":fotografia})

def imagem(request, fotografia_id):
    fotografia = get_object_or_404(Fotografia, pk=fotografia_id)
    return render(request, "gallery/imagem.html", {"fotografia": fotografia})
