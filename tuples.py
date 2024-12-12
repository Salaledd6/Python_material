#Tuples are used to store multiple items in a single variable.
#Tuples are written with round brackets
#Tuple is a collection which is ordered and unchangeable.

#So tuples should be used when the order is important
#but the data does not need to be changes

courses = ('History', 'Math', 'Physics', 'CompSci') #Defining a tuple

print(courses)  #Prints the tuple

print(courses[1]) #We can access any index of the tuple and print the value
                  #just like with the list

print(courses.index('History')) #And aswell as search for the value specified and tell it's index

print(courses.count('Math')) #Return the number of times the value 'Math' appears in the tuple

# courses.append('Art') #We cant add a value to a tuple
# courses.remove('Physics') #Neither remove
