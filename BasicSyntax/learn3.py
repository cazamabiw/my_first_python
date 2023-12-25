#Building a better calculator
num1 = float(input("Enter first number: ")) #convert string into float
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("Invalid operator")

#Dictionaries
#key value pair
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions["Dec"]) #key
print(monthConversions.get("TestKey","Not a vaild Key"))

#While loop
i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")

#Building a Guessing Game
#while loop and if condition
secret_word = "Dog"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!")

#For loop
dogs = ["Soju","Mumu","Grink"]

for index in range(len(dogs)):
    print(dogs[index])


for index in range(5):
    if index == 0:
        print(str(index) + " First Iteration")
    else:
        print(str(index) + " Not first")

#Exponent function
#easy power function
def raise_to_power(base_num,pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2,3))

#2D Lists and Nested loop
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

#[0][0] row0 column0
for row in number_grid:
    for col in row:
        print(col)

#Build a Translator
#Any vowel will become b
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "B"
            else:
                translation = translation + "b"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a pharse: ")))

