#Creating Lists and formatting lists
Age = [21,32,7,5,'Forty two','Twenty nine',50,0.5]
print(type(Age))
print('Hello!')

#Accessing elements within the list
print('hello'[0])
print('hello'[1])
print('hello'[2])
print('hello'[3])
print('hello'[4])

#print('hello'[5]) #Index Error since there isn't no index 5
print('hello'[:2])

#Slicing: Doesn't work with the index, It starts from 1
print('hello'[-2])
print('hello'[-4])

#Method Under List
methods = ['adding elements (append, insert, extend)',
           "Deleting elements(remove, pop, clear)", 
           "Other functions (index, count, sort)" ]
print("methods")

#Adding Elements
Age.append([10,29]) #takes everything as one variable and adds it to the list
print(Age)
Age.extend([10,29]) #takes everthing as seperate variables and adds it to the list
print(Age)
Age.insert(0,30) #(0=index, 30=new list number to be inserted)
print(Age)

#Deleting Elements
red = [1, 20, 'bye', 0.5, 10]
red.pop() #takes out the last element of the list
print(red)

red.remove('bye')#remove "bye from the list"
print(red)

red.clear() #clears the list
print(red)

#Sort function
green = [1, 20,0.5,10]
print(green)
green.sort() #arranges the list in ascending order
print(green) 
#green.sort(reversed) #arranges the list in ascending order
#print(green)

#count functiom
print(green.count(10))#used to count the frequency of an element in a list

#Index Function
print(green.index(10)) #Shows the position of an element in a list


#Classwork
Ben = [1,2,3,4,5,6]

#printing aa section of a list
print(Ben[1:3])

#printing to a point in a list
print(Ben[:3])

import sys
print(sys.version)