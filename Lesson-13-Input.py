

myList = []
msg = ""
while msg != 'STOP'.upper():
    msg = input("Enter new item, and STOP to finish ")
    myList.append(msg)

print(myList)

print('===============================')
name = input("Please enter Your name: ")
print("Hello " + name)

#input reads only strings, not numbers
num1 = input("Enter 1st number: ")
num2 = input("Enter 2nd number: ")

#converting to numbers
sum = int(num1) + int(num2)
print(sum)

message = ""
while message != 'secret':
    message = input("Please Enter Your Password ")
    if message == 'secret':
        break
    print("You Entered Wrong Password ")
print("Password accepted: Please wait")

