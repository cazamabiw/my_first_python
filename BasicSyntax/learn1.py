# run with order line
#variable and data
#sneak case for variable
#difference type of data
character_name  = "Jay"
character_age  = 35
is_male  = True
print("There once was a man named " + character_name)
print("he was "+ str(character_age)+" years old. ")
character_name = "Mike"
print("He really liked the name "+character_name)
print("but didn't like being "+ str(character_age))

# #working with string
# #phrase = "Biw\nCazama"
phrase = "Biw Cazama"
print(phrase.lower().isupper())
print(len(phrase))  #len is used for tell you how many string
print(phrase[0])  #string get index starting with 0
print(phrase.index("a")) #which index of 'a' in phrase
print(phrase.replace("Biw","Bill"))

#working with number
#difference type of number
from math import *  #access to lot more math function
print(-2.0987)
print(3  * (4 + 5))
print(10 % 3)  #3.1 => reminder is 1
my_num = 5
print(str(my_num) + " my fav number") #convert num to str
my_num2 = -5
print(abs((my_num2)));
print(pow(3,2))
print(max(4,6,5,53,4))
print(round(3.5)) # less than 5 round down, grater or equal 5 round up
print(floor(3.7)) # round down
print(ceil(3.7)) #round up

# #get input from user
name = input("Enter your name: ") #allow user type
age = input("Enter your age: ")
print("Hello "+ name + "! You are "+ age)

#Building a basic caculator
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
#result = num1 + num2 #num1 = 4 num2 =3   result is 43
# result = int(num1) + int(num2)
result = float(num1) + float(num2)
print(result)

#mad libs game
color = input("Enter a color")
plural_noun = input("Enter a Plural Noun")
person = input("Enter a person")
print("Roses are "+ color)
print(plural_noun+"are blue")
print("I love "+person)
