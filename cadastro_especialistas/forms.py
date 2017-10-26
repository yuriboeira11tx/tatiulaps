from django import forms
from cadastro_incidente.models import Incidente
from cidades.models import Cidade

class IncidenteForm(forms.ModelForm):
    class Meta:
        model = Incidente
        fields = ('cidade','tipo','data_prevista','gravidade')
