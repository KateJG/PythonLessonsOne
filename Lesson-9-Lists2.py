
#       0       1       2       3       4
cars = ['bmw', 'vw', 'seat', 'skoda', 'mercedes']

for x in cars:
    print (x.upper())

print("------------------")

for x in range(1, 6):
    print(x)

mynumber_list = list(range(0, 10))
print(mynumber_list)
print("=====================================")

for x in mynumber_list:
    x = x * 2
    print(x)

mynumber_list.sort(reverse=True)
print(mynumber_list)

print("Max number is : " + str(max(mynumber_list)))
print("Min number is : " + str(min(mynumber_list)))
print("Sum of list in mynumber_list is : " + str(sum(mynumber_list)))

print("=====================================")

#       0       1       2       3       4
cars = ['bmw', 'vw', 'seat', 'skoda', 'mercedes']

myCars = cars[1:4]
print(myCars)

myCars = cars[:3]
print("Example from the beginning of the list(from 0 to 4): " + str(myCars))

myCars = cars[-3:-1]
print(myCars)