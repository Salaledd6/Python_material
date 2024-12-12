#Lists are used to store multiple items in a single variable.
#Lists are created using square brackets
#Lists are mutable


courses = ['History', 'Math', 'Physics', 'CompSci'] #Defining list


print(courses) #prints the list

print(courses[0]) #Access the first index of the list and prints the value

print(courses[-1]) #Access the last index of the list and prints the value.
                   # You can also use [3], but lot of the time it's  more convenient
                   # using a negative index when not sure of how many values are being stored

courses.append('Art') #adds a value "Art" at the end of the list
print(courses)

courses.insert(0, 'Pe') #Same thing as append, but it takes an argument of index
print(courses)                         # where you want to add the value in the list.

courses_2 = ['Chemistry', 'english'] #Defines a second list

courses.extend(courses_2)           #Adds the courses_2 list to courses
print(courses)

courses.remove('Math') #Removes the value specified from the list
print(courses)

courses.pop() #Removes the last value of the list by default.
              #It holds the value removed
print(courses)

popped = courses.pop()
print(popped) # prints the value that was popped off the list

courses.reverse() #Reverses the list
print(courses)

courses.sort()  #Sorts the list in an alphabetical order
print(courses)

nums = [1,5,2,4,3] #numbers can also be used as list values

nums.sort()
print(nums)

courses.sort(reverse=True) #Sorts the list in reverse/descending order
nums.sort(reverse=True) #Sorts the list in reverse/descending order

print(courses)
print(nums)

print(courses.index('History')) #Search for the value specified and tells it's index

#print(courses.index('Math'))    #ValueError when you try to find a index of a value
                                #that does not exist

print('History' in courses) #Checks if the value is in the list and returns either True or False
                            #Useful. when dealing with conditionals and if statements.
                            #Can be also used to loop through the values of a list by using a for loop


for course in courses:        #Looping through each value of a list
    print(course)             #prints out each item of the list. Runs the code 5 times in total

for index, course in enumerate(courses):  #Enumerate function                        
    print(index, course)                  #returns the index we're at
    
print("")
for index, course in enumerate(courses, start=1): #Starts at index 1 instead of 0
    print(index, course)

course_str = ', '.join(courses) #Turns a list of courses to comma separated string values
print(course_str)

new_list = course_str.split(' - ') #Turns a string back to a list
print(new_list)