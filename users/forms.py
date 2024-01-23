from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Nome de Login",
        required = True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Ex.: Luciano Sousa",
            }
        ),
    )

    password=forms.CharField(
        label="Senha",
        required = True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Digite sua Senha",
            }
        ),
    )

class CadastroForm(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome de Cadastro",
        required = True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class" : "form-control ",
                "placeholder" : "Ex.: Luciano Sousa",
            }
        ),
    )

    email = forms.EmailField(
        label="Email",
        required = True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class" : "form-control",
                "placeholder" :" Ex.: luciano.sousa@xpto.qq",
            }
        ),
    )

    password=forms.CharField(
        label="Senha",
        required = True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class" : "form-control col-6",
                "placeholder" : "Digite sua Senha",
            }
        ),
    )

    password2=forms.CharField(
        label="Confirmar Senha",
        required = True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class" : "form-control col-6",
                "placeholder" : "Confirme Sua Senha",
            }
        ),
    )
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")
        if nome:
            nome = nome.strip()
            if " " in nome: raise forms.ValidationError("Espaços não são permitidos ness campo.")
            else: return nome
        
    def clean_password2(self):
        senha = self.cleaned_data.get("password")
        senha2 = self.cleaned_data.get("password2")
        if senha and senha2:
            if senha != senha2: raise forms.ValidationError("As senhas não são iguais!")
            else: return senha2