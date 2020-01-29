#!/usr/bin/env python

d1 = dict()  # new, empty dict
d2 = {'color': 'red', 'state': 'Wisconsin',
      'sport': 'Quidditch'}
d3 = {}

airports = {
    'EWR': 'Newark',
    'MCI': 'Kansas City',
    'RDU': 'Raleigh-Durham',
    'PIT': 'Pittsburgh',
    'LAX': 'Los Angeles',
    'SJC': 'San Jose',
    'YYC': 'Calgary',
    'YOW': 'Ottawa',
    'MCO': 'Orlando',
    'ABQ': 'Albuquerque',
    'YYZ': 'Toronto',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'IAD': 'Dulles',
    'SFO': 'San Francisco',
}

print(airports['SJC'])
for code in 'YYZ', 'YYC', 'YOW':
    print(airports[code])
print()

print(airports.get('PHL'))
print(airports.get('PHL', 'NO SUCH AIRPORT'))

airports['PHL'] = 'Philadelphia'
airports['PDX'] = 'Portland'

del airports['RDU']

print(airports)

more_airports = {
    'ELM': 'Elmira',
    'ORD': "O'Hare",
    'OAK': 'East Bay',
}

airports.update(more_airports)

print(airports)

print(len(airports))

for abbr, airport in airports.items(): # [(k,v),(k,v),...]
    print(abbr, airport)
print()

for k in 'YYZ', 'YYC', 'OMG', 'LOL', 'PIT':
    print(k, k in airports)
print()


