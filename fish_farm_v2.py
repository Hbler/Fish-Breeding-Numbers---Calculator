# -*- coding: utf-8 -*-
# Fish Breeding System Status

def sys_status_lbs(mass):
	'''Calculates the breeding system current status
	based in the mass (pounds) entered.'''

	feedRate = mass * 0.015
	tSize = feedRate * 200 # tank size.
	bVolume = feedRate * 0.67 # volume of beads in the filter.
	flowRate = feedRate * 7.5 # adequate recirculation flow.
	# Results
	print '\nBased in this weight, these are the current values of the breeding:'
	print '''
	The feeding rate in this stage is: {: .2f}lbs per day;
	The tank should be of, at least: {: .2f} gallons;
	The filter should have at least: {: .2f}ftˆ3 of beads;
	The recirculation flow should be of: {: .2f}gpm.
	'''.format(feedRate, tSize, bVolume, flowRate)
	print 'All these numbers have a safety factor.'
	print 'And are calculated for a tank equiped with a bead filter.\n'
	return

def fish_status(l):
	'''Calculates the estimated weight(g) of a fish based in its lenght.
	And based in this weight, calculates the ammonia(mg) produced in 24h.
	l = length in inches | w = weight in grams | a = miligrams of ammonia / 24h
	'''

	w = 0.28 * (l ** 2.9946)
	a = w / 5

	print '\n Based in this length, these are the estimated values:'
	print '''
    Fishes with this legth weight around {: .2f} grams, and produce
    about {: .2f}mg of ammonia per 24 hours.
	'''.format(w, a)
	print 'These values may vary between 25 and 50 percent for more or less,'
	print 'depending of the fish aspect (less if "Thin", more if "Fat").'
	return

def valid_float_input(u_input):
	'''Tests if the user input can be converted to float.'''

	try:
		float(u_input)
		return True
	except ValueError:
		print 'Invalid value. Try again.'
		return False

def get_total_mass():
	'''Gets the input of the user and tests it.'''
	while True:
		total_fWeight = raw_input (
			'\nEnter the total weight of fish in the tank in Lbs (pounds): ')
		if valid_float_input(total_fWeight):
			print 'Calculating...'
			break
	return total_fWeight

def get_size():
	'''Gets the input of the user and tests it.'''
	while True:
		fLength = raw_input (
			'\nEnter the lenght of the fish in inches: ')
		if valid_float_input(fLength):
			print 'Calculating...'
			break
	return fLength

fish_status(float(get_size()))

sys_status_lbs(float(get_total_mass()))
