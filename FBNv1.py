# -*- coding: utf-8 -*-
# Fish Breeding Numbers

# Calculates safe values for the breeding of fish
# in tanks equipped with bead filters.

# Request weigh of fish in the tank.

fWeight = float(raw_input (
	'Enter the weigh of fish in the tank in Lbs (pounds): '))

def statsCalculator(mass):
	feedRate = mass * 0.015
	tSize = feedRate * 200 # tank size.
	bVolume = feedRate * 0.67 # volume of beads in the filter.
	flowRate = feedRate * 7.5 # adequate recirculation flow.
	# Results
	print
	print 'Based in this weigh, these are the current values of the breeding:'
	print '''
	The feeding rate in this stage is: {: .2f}lbs per day;
	The tank should be of, at least: {: .2f} gallons;
	The filter should have at least: {: .2f}ftˆ3 of beads;
	The recirculation flow should be of: {: .2f}gpm.
	'''.format(feedRate, tSize, bVolume, flowRate)
	print '''All these numbers have a safety factor.
And are calculated for a tank equiped with a bead filter.
	'''

statsCalculator(fWeight)
