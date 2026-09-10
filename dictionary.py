#Python Dictionary Basics
student = {
    "name" : "Rani burra", 
    "subject" : {
        "phy" : 97,
        "chem" : 98,
        "maths" : 96,
    }
}
print(student.keys()) #return all the keys
print(list(student.keys()))
print(len(list(student.keys())))
print(list(student.values())) # return all the values
print(list(student.items())) #return all (keys, values) pairs as tuple

pairs = list(student.items())
print(pairs[0])

print(student.get("name")) #return the key according to values

student.update({"city" : "Bhopal"}) #insert the specified item to the dictionary
print(student)