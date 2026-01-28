#hello world program
print("Hello world")

#Variable task 1
age = 21           #num
name = "shabu"       #text
print(age)
print(name)

#Data Types int

age = int(input("Enter your age: "))   
print("Your age is:", age)
 #float

heat = float(input("Enter the temperature: "))  # Convert input to float
print("The temperature is:", heat)
#String

city = input("Enter your city: ")
print(city)
#boolean

student = input("Are you a student? y/n: ").strip().lower()  
if student == "y":
 print(True)
else:
 print(False)