#Try except
try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")

#File management
#Reading Files
#mode r = read , w = write (over writing), a = append, r+ = read and write
employee_file = open("employee.txt", "r")
if employee_file.readable(): #check this file can read or not
    for employee in employee_file.readlines():
        print(employee)
else:
    print("Cannot read the file")
employee_file.close()

#Writing to Files
employee_file = open("employee.txt", "a")
employee_file.write("\ntest employee line3")
employee_file.close()

#Modules & Pip
#https://pymotw.com/3/py-modindex.html
#pip is the package installer for Python. It is a tool that allows you to install and manage Python packages,