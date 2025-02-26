def type_greetings(name):
    "Print Greeting"
    print("Congratulations " + name +" , wish you all the best!")

def mysum(x, y):
    s = (x + y)
    return s


# Factorials 1! = 1*1, 2! = 1*2, 3! = 1 * 2 * 3, 4! = 1 * 2 * 3 * 4
def factorial(x):
    """Calculate Factorial of number X"""
    answer = 1
    for i in range(1, x + 1):
        answer = answer * i
    return answer

for i in range(1, 10):
    print(str(i) + "!\t = " + str(factorial(i)))

print(factorial(4))
print(factorial(5))


print("-----------------------------")

type_greetings('Kate')
type_greetings('Lucas')
type_greetings('Vaiva')

x = mysum(5, 4)
print(x)


