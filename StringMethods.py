name = "Mukuwa"
tree = "oak"
idol = "TAEMIN"
numbers= "123"
food = "salsa"

#print the length of name variable
print(len(name))
#'length method' --> will print and return the length of the variable
#since name is equal to Mukuwa it will return six characters

#find method
print(name.find("Mu"))
#to find the first instance of the letters "Mu"--> will be located at
#index 0 because computers always start at index 0

#captialize method
print(tree.capitalize())
#will print the value of the object to the console while capitalizing output

#uppercase method
print(tree.upper())
#will make all characters within the object printed to console in uppercase

#lowercase method
print(idol.lower())
#will print all characters in lowercase

#isDigit method
print(numbers.isdigit())
print(name.isdigit())
#will verify is value of object is numerical with true or false

#isAlpha method
print(name.isalpha())
print(numbers.isalpha())
#will varify if object contains alphabetical characters: True or False output

#count method
print(name.count("u"))
#counts how many characters are in your string (within object)
#Searches for the amount of u's in Mukuwa (in object 'name') --> 2 (output)

#replace method
print(food.replace("a","i"))
#places characters within a string
#has two arguments, the old string (,) and the new string
#will make 'salsa' --> 'silsi

#Multiple prints
print(name*3)
#Will print Mukuwa three times in the console
