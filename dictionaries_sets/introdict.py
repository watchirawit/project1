phonebook = {'wachirawit':'777-1111','Mickey':'777-2222','Donald':'777-3333'}

print(phonebook)

print(phonebook['Mickey'])
print(phonebook['Donald'])

key = 'Pluto'
if key in phonebook:
    print(phonebook['Pluto'])
else:
    print(key + ' not in phonebook')

phonebook['Simpson'] = '777-4567'
phonebook['Pluto'] = '777-4444'
phonebook['Mickey'] = '777-2122'

del phonebook['Simpson']
print(phonebook)