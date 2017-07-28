from django.shortcuts import render

from city.forms import LocalizacaoForm
from city.models import Setor


def index(request):
    form = LocalizacaoForm()
    setor = Setor.objects.all()

    context = {
        'form': form,
        'setor': setor,
    }

    return render(request, 'index.html', context)
