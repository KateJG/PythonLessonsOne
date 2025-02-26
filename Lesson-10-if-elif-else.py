#
age = 12

if (age <= 2):
    print("You are baby!")
elif (age > 2) and (age < 12 ):
    print("You are kid")
elif (age >= 12) and (age < 19):
    print("You are teenager")
else:
    print("You are adult")

print("-------EOF-----")

all_cars = ['Rolls Roys', 'KIA', 'dacia', 'bmw', 'audi', 'ford', 'mercedes-benz', 'Jaguar']
german_cars = ['bmw', 'audi', 'mercedes-benz']

if 'dacia' in all_cars:
    print("Yes, dacia is in the list")
else:
    print("Dacia is NOT in the list")

print("---------------------------------------------------")

all_cars = ['Rolls Roys', 'KIA', 'dacia', 'bmw', 'audi', 'ford', 'mercedes-benz', 'Jaguar']
german_cars = ['bmw', 'audi', 'mercedes-benz']

for x in all_cars:
    if x in german_cars:
        print(x + " is German Car")
    else:
        print(x + " is not a German Car")




