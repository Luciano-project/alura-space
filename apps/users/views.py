from django.shortcuts import render, redirect
from apps.users.forms import LoginForms, CadastroForm
from django.contrib.auth.models import User
from django.contrib import auth, messages


# Create your views here.
def login(request):
    form = LoginForms()
    redirection = ''
    if request.GET:
        if not request.method == "POST": messages.error(request, "Usuário não autenticado!")
        redirection=request.GET["next"]
        
    if request.method == "POST":
        form = LoginForms(request.POST)
        if form.is_valid():
            nome=form["nome_login"].value()
            senha=form["password"].value()
            usuario = auth.authenticate(
                username=nome,
                password=senha
            )
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f"{nome} logado com sucesso!")
                if redirection: return redirect(redirection)
                return redirect('index')
            else:
                messages.error(request, "Credenciais incorretas")
                return redirect('login')
    return render(request, "users/login.html", {"form":form, "redirect_get":redirection}) 

def cadastro(request): 
    form = CadastroForm()
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            nome=form["nome_cadastro"].value()
            email=form["email"].value()
            senha=form["password2"].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, "usuario já existe")
                return redirect('cadastro')
                # nome de usuario já existente
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, "Novo usuário cadastrado com sucesso!")
            return redirect('login')
            #print(nome,email,senha)
        
    return render(request, "users/cadastro.html", {"form":form}) 

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect('login')