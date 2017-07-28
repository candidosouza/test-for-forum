from django.contrib import admin

# Register your models here.
from city.models import Setor, SubSetor

class SetorAdmin(admin.ModelAdmin):
    list_filter = ['nome']
    list_display = ('id', 'nome')


class SubSetorAdmin(admin.ModelAdmin):
    list_filter = ['nome']
    list_display = ('id', 'nome','setor')

admin.site.register(Setor, SetorAdmin)
admin.site.register(SubSetor, SubSetorAdmin)