#variable = a container for a value
#behaves as the value it contains

#String - a sequence of character (data type)
#needs double or single quotes

name = "bro"
#sets the value of the variable to a String data type by name of bro

print(name)
#prints the value of string to the console window

print("hello "+name)

#How to check the data type of a variable
#use the 'type' function
print(type(name))
#will say <class 'str'> --> declaring that the data type is string

first_name= "Mukuwa "
#is you have a variable that has a space in it, use an underscore
last_name = "Baffoe"
full_name = first_name + last_name
print("Hello"+ full_name)

#int = integer (data type)
age = 25
age = age + 1 # increases the value of age variable by one
print(age)
#shortcut

age += 1 #shorthand way to increase value
print(age)
print(type(age)) # will print <class 'int'>

#important to use right data type, cannot mix

#have to convert int variable to a string in order to print it with a string literal
print("Your age is " +str(age)) #this converts int into string literal
#cannot store decimal numbers

#Float data type
#short for floating point number
#can store decimal numbers unlike integer data type

height = 5.5
print(height)
print(type(height))#check variable type
print("Your height is "+str(height)+" ft")

#boolean (data type)
#variable that can only store true or false

human = True
alien = False

print(human)
print(alien)
print(type(human)) #checks data type
print("Are you a human? " + str(human))