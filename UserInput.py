
input("What is your name?: ")


#assign the user input to a variable ---> can use elsewhere
location = input("Where do you live?: ")
#create a new variable, the user input will then be stored in the variable
print("Wow that's great! "+location+" is such a beautiful place!")

#When you accept user input it is always of the string data type
#to accept a number you have to convert input to another data type

age = int(input("How old are you?: "))
#surround user imput with a type cast [int] --> converts to int data type
print("You're "+str(age)+"? You don't say...")
#cannot concatinate two different data types, so you will have to
#covert the integer data type back to a string to display it in
#terminal window

height = float(input("How tall are you?: "))
print("You are "+str(height)+" feet tall")