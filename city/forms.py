from django import forms
from city.models import Localizacao


class LocalizacaoForm(forms.ModelForm):
    class Meta:
        model = Localizacao
        fields = ('setor', 'subsetor', 'nome')

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'setor': forms.TextInput(attrs={'class': 'form-control'}),
            'subsetor': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'nome': "Nome",
            'setor': "Setor",
            'subsetor': "Sub-setor",
        }
