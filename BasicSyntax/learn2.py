#lists
#list in python can be various data in the same list
friends = ["Kevin","Karen","Jim","Bill","Tony"] #index start with 0
print(friends[1]) #if use -number like -1 it will start with last element = Tony
print(friends[1:3]) #start in 1 to .. not include index 3
friends[1] = "Bo" #add Bo instead of Karen
print(friends[1:3])

# #list function
lucky_number = [4,8,15,16,23,42]
friends = ["Kevin","Karen","Jim","Bill","Bill","Bo"]
#friends.extend(lucky_number) #addrange
friends.insert(1,"Kelly") #index 1 = Kelly, other elements will push to the right
friends.remove("Jim")
friends.pop() #remove the last element in the list
print(friends.index("Kevin")) #check Kevin in list or not to show the index
#friends.clear() #clear list
print(friends)
print(friends.count("Bill")) #count Bill in list
friends.sort() #sort alphabet order (asc)
print(friends)
lucky_number.reverse() #order by desc
print(lucky_number)
friends2 = friends.copy(); #copy friends list

# #Tuple
#type of datastructor = container store difference value
#emuable = tuple can't change or modify element
coordinates = (4,5)
coordinates2 = [(4,5),(3,4),(5,2),(10,3)] #tuple in list, so they can modify
coordinates2[0] = (3,3);
print(coordinates2[0]);
print(coordinates[0]) #print index 0 in tuple
#between list and tuple => list can modify, tuple can't do that

#Functions
#collection of code, that take specific task
def say_hi(name,age): #also sneak case #code inside function need to be indented
#for param can pass in any type
    print("Hello User "+name +", you are "+str(age))
#call funtion
print("top")
say_hi("Bill",34)
print("bottom")

#Return statement
#return info. from function
def cube(num):
    return num*num*num
    print("code") #not run this line because it already return

result = cube(3)
print(result)

#if statements
is_human = False
is_tall = False
if is_human and is_tall: #use indented
    print("You are a human or tall or both")
elif is_human and not(is_tall):
    print("You are a short human")
elif not(is_human) and is_tall:
    print("You aren't a human but are tall")
else:
    print("You are either not human or not tall or both")

#if statements and comparison
def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return  num3

print(max_num(300,4,5))

