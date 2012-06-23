from django.db import models
#-*- coding: utf-8 -*#-

class Criterios_ergonomicos(models.Model):
	criterio = models.CharField('Criério', max_length=100)
	descricao = models.TextField('Descrição',)
	
	class Meta:
		verbose_name = u'Critério ergonômico'
		verbose_name_plural = u'Critérios ergonômicos'
	
	def __unicode__(self):
		return self.criterio
"""
class Tipo(models.Model):
	TIPO_CHOICES = (
		('SIMNAO', (
			('sim', 'Sim'),
			('nao','Não'),
			)
		),
		( 'GRADUADA', (
			('0', '0'),
			('1', '1'),
			('2', '2'),
			('3', '3'),
			('4', '4'),
			('5', '5'),
			)
		),
	)
	
	valor = models.CharField(choices = TIPO_CHOICES, max_length=3)
	tipo = models.CrarField(choices = TIPO_CHOICES, max-length=3)

	def __unicode__(self):
		return self.valor
	"""	
class Elementos_de_interacao(models.Model):
	nome = models.CharField('Nome', max_length=100)
	
	def __unicode__(self):
		return self.nome
		
	class Meta:
		verbose_name = u'Elemento de interação'
		verbose_name_plural = u'Elementos de interação'

class Questoes(models.Model):
	criterio_ergonomico = models.ForeignKey(Criterios_ergonomicos)
	enumciado = models.CharField('enumciado', max_length=200)
	descricao = models.TextField('Descrição',)
	#valor = models.ForeignKey(Tipo)
	#tipo = models.CharField()
	elementos_de_interacao_associados = models.ForeignKey(Elementos_de_interacao)
	
	def __unicode__(self):
		return self.enumciado
		
	class Meta:
		verbose_name = u'Questão'
		verbose_name_plural = u'Questões'