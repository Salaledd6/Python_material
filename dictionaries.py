#Dictionaries are used to store data values in key:value pairs.
#Dictionary is a collection which is ordered*. changeable and do not allow duplicates
#Dictionaries are written with curly brackets, and have keys and values:

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']} #Defined a dictionary
#contains three key-value pairs:
#'name' with the value 'John'
#'age' with the value 25
#'courses' with the value ['Math', 'CompSci']



print(student) #Prints out a dictionary. All the keys and values
print(student['name']) #Prints out a value of key 'name'. Gives an error when key does not exits

print(student.get('phone')) #Same thing, but instead of an error it returns 'none' by default

print(student.get('phone', 'Not Found')) #Returns a 'Not Found' for keys that don't exist

student['phone'] = '555-5555' #Adding a new key:value pair to dictionary

print(student.get('phone'))
print(student)

student['name'] = 'Jane' #If a key already exist. it will update the value of that key
print(student) 

student.update({'name': 'James', 'age': 20, 'phone': '555-5555'}) #Updates values. Useful when updating multiple values at a time                                                         #multiple values at a time 
print(student)

del student['age'] #Removes the value specified
print(student)
 
phone = student.pop('phone') #Removes, but also returns the value which allows to grab the removed value with a variable
print(phone)
print(student)

print(len(student)) #Checks how many keys is in dictionary

print(student.keys()) #See the keys

print(student.values()) #See the values

print(student.items()) #See the key:value pairs

for key in student: #Loops through keys
    print(key)

for key, value in student.items(): #loops through keys and values
    print(key, value)