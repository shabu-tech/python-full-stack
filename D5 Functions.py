#A function is a block of code that performs a task
#declare
def greet():
    print("Hello")
greet()
#function with parameter
def greet(name):
    print("Hello, " + name )

greet("SHABANA")
greet("SHAJAHAN")
#function with return value
def add(a,b):
    return(a+b)
a=int(input())
b=int(input())
result=add(a,b)
print(result)
#check if a number is even
def even(num):
    if num % 2 == 0:
        return True
    else:
        return False
number = int(input())
print(even(number))


