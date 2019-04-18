"""
<ASCII Table for rotational values, >
URL : https://inventwithpython.com/chapter14.html
"""

rotationtype = input('Enter rot5, rot13 or rot47: ') #user input, rotation type
userinput = input('Enter cypher: ') #user input, enter string
userlist = list(userinput) #converting string to a list of characters

def rot5(): #rot5 function
    for x in range(0,10): #shifts once then increments
        for y in userlist: #loops through a list of characters
            print(chr(48 +((ord(y) - 48) + x) %10), end='') #rot5 algorithm (ASCII Table, each number represents a specific string value or number)
        print('') #makes a new print statement and prints out the output vertically

def rot13(): #rot13 function
    for x in range(0,26): #shifts once then increments
        for y in userlist: #loops through a list of characters
             print(chr(97 +((ord(y) - 97) + x) %26), end='') #rot13 algorithm (ASCII Table, each number represents a specific string value or number)
        print('') #makes a new print statement and prints out the output vertically

def rot47(): #rot47 function
    for x in range(0,94): #shifts once then increments
        for y in userlist: #loops through a list of characters
            print(chr(33 +((ord(y) - 33) + x) %94), end='') #rot47 algorithm (ASCII Table, each number represents a specific string value or number)
        print('') #makes a new print statement and prints out the output vertically

if rotationtype == 'rot5':
    print(rot5())
elif rotationtype == 'rot13':
    print(rot13())
elif rotationtype == 'rot47':
    print(rot47())
else:
    print('invalid rotation type')
