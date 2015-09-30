# -*- coding: utf-8 -*-
# Fish Breeding System Status

# Calculates safe values for the breeding of fish
# in tanks equipped with bead filters.

def statusCalculatorLbs(mass):
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

def valid_mass(u_input):
	'''Tests if the user input can be converted to float.'''

	try:
		float(u_input)
		return True
	except ValueError:
		print 'Invalid value. Try again.'
		return False

def get_mass():
	'''Gets the input of the user and tests it.'''
	while True:
		fWeight = raw_input (
			'Enter the total weight of fish in the tank in Lbs (pounds): ')
		if valid_mass(fWeight):
			print 'Calculating...'
			break
	return fWeight

statusCalculatorLbs(float(get_mass()))
