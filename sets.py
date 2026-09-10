#python Sets Basics
collection = {1, 2, 2, 2, "Hello", "World", "Hello"}
print(collection)
print(type(collection))
print(len(collection))

#Tupl Methods
collection.add(3) # add the element
collection.remove(1) #remove the element
collection.pop() #remove random value

#Union and Intersection
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2))
print(set1.intersection(set2))