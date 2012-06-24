from django.contrib import admin
from .models import Criterios_ergonomicos, Elementos_de_interacao, Questoes

class QuestoesAdmin(admin.ModelAdmin):
	list_display = ('criterio_ergonomico', 'enumciado', 'descricao', 
	                'elementos_de_interacao_associados', 'tipo') 


admin.site.register(Questoes, QuestoesAdmin)
admin.site.register(Elementos_de_interacao)
admin.site.register(Criterios_ergonomicos)