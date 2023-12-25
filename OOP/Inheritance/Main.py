from Chef import Chef
from ThaiChef import ThaiChef


# Instantiate an object of the Chef class with a name
myChef = Chef("Chef Salt Bae")

# Access and print the name using the getter method
print("Chef's Name:", myChef.get_name())

# Use the setter method to change the name
myChef.set_name("Chef Jamie Oliver")

# Access and print the updated name using the getter method
print("Updated Chef's Name:", myChef.get_name())

# Encapsulation: Call a method to demonstrate encapsulation of behavior
myChef.make_special_dish()

# Instantiate an object of the ThaiChef class
myThaiChef = ThaiChef("Chef Ian Kittichai")
print("Chef's Name:", myThaiChef.get_name())
# Encapsulation: Call methods to demonstrate encapsulation of behavior
myThaiChef.make_salad()
myThaiChef.make_special_dish()
myThaiChef.make_tom_yum_kung()