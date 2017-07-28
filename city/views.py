from django.http import HttpResponse
from django.shortcuts import render

import json

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


def get_subsetor(request, setor_id):
    setor = Setor.objects.get(pk=setor_id)
    subsetores = setor.subsetor.all()
    subsetores_dict = {}
    for subsetor in subsetores:
        # if your subcategory has field name
        subsetores_dict[subsetor.id] = subsetor.nome
    return HttpResponse(json.dumps(subsetores_dict), content_type="application/json")
