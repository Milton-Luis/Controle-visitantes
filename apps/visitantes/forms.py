from django import forms
from apps.visitantes.models import Visitantes


class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitantes
        fields = ["nome", "cpf", "data_nascimento", "numero_casa", "placa_veiculo"]

        error_messages = {
            "nome": {"required": "O campo nome é obrigatório"},
            "cpf": {"required": "O campo cpf é obrigatório"},
            "data_nascimento": {
                "required": "O campo data de nascimento é obrigatório",
                "invalid": "informe a data em um formato válido (DD/MM/AAAA)",
            },
            "numero_casa": {"required": "O campo número da casa é obrigatório"},
        }

class AutorizaVisitanteForm(forms.ModelForm):

    morador_responsavel = forms.CharField(required=True)

    class Meta:
        model = Visitantes
        fields = [
            "morador_responsavel"
        ]

        error_messages = {
            "morador_responsavel":{
                "required": "Informe o nome do morador responsável por autorizar a entrada do visitante"
            }
        }