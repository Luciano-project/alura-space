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