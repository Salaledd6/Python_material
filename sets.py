#Sets are used to store multiple items in a variable.
#Sets are written with curly brackets.
#Set is a collection which is unordered. Items in a set don't have a defined order
#They appear in a different order every time you use them, and cannot be referred by index.    
#Set items are unchangeable, but you can remove and add new items.
#Set cannot have two items with the same value

courses = {'History', 'Math', 'Physics', 'CompSci'} #Defining a set
art_courses = {'History', 'Math', 'Art', 'Design'} 

print(courses) #Prints the set in a random order

print('History' in courses) #Checks if the value is in the list and returns either True or False

print(courses.intersection(art_courses)) #Returns a set, that is the intersection (Same values) of two sets

print(courses.difference(art_courses)) #Returns a set containing the difference between the art_courses
print(courses.union(art_courses))      #Returns a set containing values of both sets

courses.add('English')  #Adds a value to the set
print(courses)

courses.clear()     #Removes all the values from the set (takes no arguments)
print(courses)

art_courses.discard('Design') #Removes a specific value from the set


art_courses.remove('Math') #Removes a specific value from the set
                           #Different form the Discard() method, because this method
                           #will raise an error if the specified value does not exist
print(art_courses)

art_courses.pop() #Removes a random value from the set (takes no arguments)
print(art_courses)

courses.update(art_courses)
print(courses)
