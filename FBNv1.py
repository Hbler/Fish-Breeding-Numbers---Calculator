# -*- coding: utf-8 -*-
# Fish Breeding Numbers

# Calculates safe values for the breeding of fish in tanks equipped with bead filters.

# 1. Request weigh of fish in the tank. 

fWeigh = input ('Type the weigh of fish in the tank in Lbs (pounds): >> ')


# 2. Calculates the feeding rate

feedRate = fWeigh * 0.015


# 3. Calculates the tank size.

tSize = feedRate * 200


# 4. Calculates the necessary volume of beads in the filter.

bVolume = feedRate * 0.67


# 5. Calculates the adequate recirculation flow.

flowRate = feedRate * 7.5

# 6. Presents the results in a way that the user can easily identify.

print
print 'Based in this weigh, these are the current values of the breeding:'
print 'The feeding rate in this stage is: {: .2f}lbs per day;'.format(feedRate)
print 'The tank should be of, at least: {: .2f} gallons;'.format(tSize)
print 'The filter should have at least: {: .2f}ftˆ3 of beads;'.format(bVolume)
print 'The recirculation flow should be of: {: .2f}gpm.'.format(flowRate)
print
print 'All these numbers have a safety factor and are calculated for a tank equiped with a bead filter.'
