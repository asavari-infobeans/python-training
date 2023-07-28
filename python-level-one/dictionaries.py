#DICTIONARIES

my_stuff = {
    'key1':'value1',
    'key2': 'value2',
    'key3': {'123':[1,2,'grabme']}
}
#To print perticular key value
print(my_stuff['key1'])

#To print whole dictionary
print(my_stuff)

#To print last key list element
print(my_stuff['key3']['123'][2])