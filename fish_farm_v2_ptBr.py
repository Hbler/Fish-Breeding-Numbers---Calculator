# -*- coding: utf-8 -*-
# Estado do Sistema de Criação de Peixes

def sys_status_kg(mass):
	'''Calculates the breeding system current status
	based in the mass (kilos) entered.'''

	feedRate = mass * 0.015
	tSize = feedRate * 757 # tamanho do tanque.
	bVolume = feedRate * 0.018 # volume necessários de "beads" no filtro.
	flowRate = feedRate * 1698 # circulação adequada.
	# Resultados
	print '\nA partir do peso digitado,',
	print 'estes são os valores atuais recomendados para a criação:'
	print '''
	A taxa de alimentação nesse estágio é de: {: .2f}g por dia;
	O tanque deve ter pelo menos: {: .2f} litros;
	O filtro deve ter pelo menos: {: .4f}mˆ3 de mídia flutuante;
	A circulação de água deve ser de: {: .2f} L/H.
	'''.format(feedRate, tSize, bVolume, flowRate)
	print 'Todos os valores tem um fator de segurança.'
	print 'E são calculados para um tanque equipado',
	print 'com um filtro de mídias flutuantes.\n'
	return

def fish_status_ptBr(l):
	'''Calculates the estimated weight(g) of a fish based in its lenght.
	And based in this weight, calculates the ammonia(mg) produced in 24h.
	l = length in inches | w = weight in grams | a = miligrams of ammonia / 24h
	'''

	w = 0.28 * ((l / 2.54) ** 2.9946)
	a = w / 5

	print '\nCom base neste comprimento, os valores estimados são:'
	print '''
	Peixes com esse comprimento pesam em torno de {: .2f} gramas,
	e produzem em média {: .2f}mg de amonia a cada 24 horas.
	'''.format(w, a)
	print 'Esses valores podem variar entre 25 e 50 por cento para + ou para -,'
	print 'dependendo do aspecto dos peixes ( - se "Magros" ou + se "Gordos").'
	return

def valid_float_input_ptBr(u_input):
	'''Tests if the user input can be converted to float.'''

	try:
		float(u_input)
		return True
	except ValueError:
		print 'Valor Inválido. Tente novamente.'
		return False

def get_total_mass_ptBr():
	'''Gets the input of the user and tests it.'''

	while True:
		total_fWeight = raw_input (
			'\nDigite o peso total de peixes no tanque em Kg (quilos): ')
		if valid_float_input_ptBr(total_fWeight):
			print 'Calculando...'
			break
	return total_fWeight

def get_size_ptBr():
	'''Gets the input of the user and tests it.'''
	while True:
		fLength = raw_input (
			'\nDigite o tamanho do peixe em centímetros: ')
		if valid_float_input_ptBr(fLength):
			print 'Calculando...'
			break
	return fLength

fish_status_ptBr(float(get_size_ptBr()))

sys_status_kg(float(get_total_mass_ptBr()))
