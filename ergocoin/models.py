'''
Copyright (c) 2012, Roberto Leite de Moraes Rodrigues, University of São Paulo
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the University of São Paulo nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL ROBERTO LEITE DE MORAES RODRIGUES AND 
UNIVERSITY OF SÃO PAULO BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, 
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED 
TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR 
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF 
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING 
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS 
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

from django.db import models
# coding: utf-8

class Criterios_ergonomicos(models.Model):
	criterio = models.CharField('Criério', max_length=100)
	descricao = models.TextField('Descrição',)
	
	class Meta:
		verbose_name = u'Critério ergonômico'
		verbose_name_plural = u'Critérios ergonômicos'
	
	def __unicode__(self):
		return self.criterio

class Tipo(models.Model):
	TIPO_CHOICES = (
		('SN', "Sim ou Não"),
		( 'GRD', "Graduada"),
	)
	
	tipo = models.CharField(choices = TIPO_CHOICES, max_length=3)

	def __unicode__(self):
		return self.tipo

class Valor(models.Model):
	VALOR_CHOICES = (
		('s', 'Sim'),
		('n','Não'),
		('0', '0'),
		('1', '1'),
		('2', '2'),
		('3', '3'),
		('4', '4'),
		('5', '5'),
	)
	
	valor = models.CharField(choices = VALOR_CHOICES, max_length=1)

	def __unicode__(self):
		return self.valor

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
	tipo = models.ForeignKey(Tipo)
	valor = models.ForeignKey(Valor)
	elementos_de_interacao_associados = models.ForeignKey(Elementos_de_interacao)
	
	def __unicode__(self):
		return self.enumciado
		
	class Meta:
		verbose_name = u'Questão'
		verbose_name_plural = u'Questões'