from django.contrib import admin
from ergocoin.models import Criterios_ergonomicos, Elementos_de_interacao, Questoes

class QuestoesAdmin(admin.ModelAdmin):
	list_display = ('Questoes', 'Elementos_de_interacao', 'Criterios_ergonomicos', 'tipo') 
	list_filter = ['Elementos_de_interacao']


admin.site.register(Questoes)
admin.site.register(Elementos_de_interacao)
admin.site.register(Criterios_ergonomicos)

