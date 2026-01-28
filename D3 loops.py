#for loop use range known
#1
for i in "apple":
        print(i)
#2
for i in range(1,6):
        print(i)

#3-print table 2
for i in range(1,11):
        print(i,"x2=",i*2)
#4 count the even and odd numbers
a = int(input())
b = int(input())
even_count = 0
odd_count=0
for i in range(a, b):
    if i%2==0:
        even_count = even_count + 1
    else:
          odd_count=odd_count+1
print("Even number count",even_count)
print("odd number count",odd_count)

#count the number are divisible by 3&5
a = int(input())
b = int(input())
count=0
for i in range(a,b):
      if(i%3==0 and i%5==0):
            count=count+1
print("No of Divisible:",count)
#Nested for loop
for i in range(1,6):
         for j in range(1,3):
                print(i,"apple")
#2
for i in range(1,3):
       print("Week:",i)
       for j in range(1,4):
         print("Day",j)
#pattern 1
for i in range(1,5):
      print("NUMBER PATTERN")
      for j in range(1,i+1):
            print(j,end="")

#pattern 2

for i in range(1, 5):            
    for j in range(1, i + 1):    
        print("*", end="")       
    print("STAR PATTERN")                       





 