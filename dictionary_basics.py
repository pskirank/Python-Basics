import pprint

numbers = {0:'Zero', 1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine'}
numbers[10] = 'Ten'                     #Basic value finding using a key.
mycat = {'size':'fat', 'color':'red', 'fur':'thick'}

print('my cat is '+ mycat['size'] + ' and it is ' + mycat['color'])
for i in mycat:
    print(i,"-",mycat[i])
for j in mycat.values():                # All values of a dictionary
    print(j)
for k in mycat.items():                 # All key value pairs of a dictionary
    print(k)
for l in mycat.keys():                  # All keys of a dictionary                
    print(l)

#dictionary.get(key, default value) - If key exist in the dictionary, it will return it's key. Else "Default value" will be returned.
print("my cat has either "+mycat.get('fur', 'dense') + ' hair or '+ mycat.get('Sweet', 'colored') + ' hair')

#Checking for an existing B'Day or adding a new entry in the DB.
birthdays = {'Alice': 'Apr 1', 'Bob':'Feb 2', 'George':'March 3', 'Robert':'April 4'}
while True:
    name = input("Enter the Name:")
    if name == '':
        print("Blank Input")
        break
    elif name in birthdays:
        print(birthdays[name] + ' is the birthday of '+name)
        break
    else:
        print("Seems your name is not in the Birthday list")
        bday = input("Enter the DOB of " + name +" :" )
        birthdays[name] = bday                              #Adding a new key, value pair to the dictionary.
        print("Database updated")
        print(birthdays)
        break

newDict = {'key1':'Value', 'key2':'Value2'}
newDict.setdefault('key2','Value2')        #If a key exists in the dictionary, it's value is returned
print(newDict)
newDict.setdefault('key3','Value3')        #If a key doesn't exist, that key value pair will be added in the dictionary.
print(newDict)


message = "Hi How R u"
count = {}
for char in message:
    count.setdefault(char, 0)
    count[char] = count[char] + 1
pprint.pprint(count)  #Pretty Print sorts the dictionary in a clean way

