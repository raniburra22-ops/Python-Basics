#Python String Basics
#Escape Sequence charater
#TYPE1
str1 = "this is a string . We are creating it in python."
print(str1)

#TYPE2
str2 = "This is a string .\n We are creating it in python. "
print(str2)

#TYPE3
str3 = "This is a string .\t We are creating it in python. "
print(str3)

#Concatenation
str4 = "Sita"
str5 = "Ram"
final_str = str4 + str5
print(final_str)

#Lenth to str
len1 = len(str4)
print(len1)
len2 = len(str5)
print(len2)
final__str = str4 + " " + str5
print(final__str)
print(len(final__str))

#Indexing
str6 = "Rani Burra"
print(str6[2])

#Slicing
print(str6[1:4])
print(str6[ :4])
print(str6[-3:-1])

#String Function
print(str1.endswith("thon.")) #return true string ends with substring
print(str1.capitalize()) # capitalize 1st char
print(str1.replace("o", "a")) #repalce all occurence of old
print(str1.find("are")) #return 1st index of 1st occurence
print(str1.count("i"))