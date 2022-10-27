from contatos.models import Contato
from django import forms

class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = () # para excluir os campos que voce nao quer que apareca no form