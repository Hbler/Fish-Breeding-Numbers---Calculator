# -*- coding: utf-8 -*-
# Números para a Criação de Peixes

# Calcula valores seguros para a criação de peixes
# em tanques equipados com filtros de mídia flutuante.

fWeight = float(raw_input (
	'Digite o peso total dos peixes no tanque em Kg(quilos): '))

def statsCalculator(mass):
	feedRate = mass * 0.015
	tSize = feedRate * 757 # tamanho do tanque.
	bVolume = feedRate * 0.018 # volume necessários de "beads" no filtro.
	flowRate = feedRate * 1698 # circulação adequada.
	# Resultados
	print
	print 'A partir do peso digitado,',
	print 'estes são os valores atuais recomendados para a criação:'
	print '''
	A taxa de alimentação nesse estágio é de: {: .2f}g por dia;
	O tanque deve ter pelo menos: {: .2f} litros;
	O filtro deve ter pelo menos: {: .4f}mˆ3 de mídia flutuante;
	A circulação de água deve ser de: {: .2f} L/H.
	'''.format(feedRate, tSize, bVolume, flowRate)
	print '''Todos os valores tem um fator de segurança.
E são calculados para um tanque equipado com um filtro de mídias flutuantes.
	'''

statsCalculator(fWeight)
