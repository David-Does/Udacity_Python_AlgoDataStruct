"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

locations = {}
locations.setdefault('North America', {})['USA'] = ['Mountain View']
locations.setdefault('Asia',{})['India'] = ['Bangalore']
locations.setdefault('North America', {})['USA'].append('Atlanta')
locations.setdefault('Africa', {})['Egypt'] = ['Cairo']
locations.setdefault('Asia', {})['China'] = ['Shanghai']

locations1 = {'North America': {'USA': ['Mountain View']}}
locations1['North America']['USA'].append('Atlanta')
locations1['Asia'] = {'India': ['Bangalore']}
locations1['Asia']['China'] = ['Shanghai']
locations1['Africa'] = {'Egypt': ['Cairo']}

def citiesInCountry(countries,userCountry):
    # print countries
    for cities in countries:
        for country in cities.keys():
            # print country
            if (country == userCountry):
                print '1'
                for city in sorted(cities[country]):
                    print city

def citiesInContinent(dict,userContinent):
    for continent in dict.keys():
         if (continent == userContinent):
            print '2'
            finalList = []
            for countries,cities in dict[continent].iteritems():
                finalList.append(cities[0] + ' - ' + countries)
            for city in sorted(finalList):
                print city


# citiesInCountry(locations.values(),'USA')
# citiesInContinent(locations,'Asia')




"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""



"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""


class HashTable(object):
    def __init__(self):
        self.table = [None] * 10000

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        asci1 = ord(string[0])
        asci2 = ord(string[1])
        return asci1*100 + asci2

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        index = self.calculate_hash_value(string)
        if (self.table[index] != None):
            if string in self.table[index]:
                return index
        return -1

    def store(self, string):
        """Input a string that's stored in
        the table."""
        index = self.calculate_hash_value(string)
        if (self.lookup(string) == -1):
            self.table[index] = [string]
        else:
            self.table[index].append(string)
        pass



# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
print hash_table.lookup('UDACITY')

# Test store
hash_table.store('UDACITY')
# Should be 8568
print hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print hash_table.lookup('UDACIOUS')
