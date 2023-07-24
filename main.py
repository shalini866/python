import math
from array import *

a ="hello World"
print(a)

# create a variable
name = 'Eric Cartman'
# print the value
print(name)

#variables and print()
city ="chennai"
print(city)
city="coimbatore"
print(city)

place ="chennai"
destination_place ="New Yok"
place = destination_place
print(place)

street = "mission st"
location = 6
print("street:",street , "location:",location)

#data types in python 
#string type
str1 = "Hello"
str2 ="World"
print(str1[0])
print(str2[-1])
print(str1[0:4])
strr = "Attachment"
print(strr.find("me"))
print(strr.replace("me","xy"))
print(strr.count("t"))


#numeric type
num1 = 5
print(num1,'is a type of ',type(num1))
num2 = 5.0
print(num2,'is a type of',type(num2))
num3 = 1+2j
print(num3,'is a type of',type(num3))
num4 = num1 < num2  # True
print(num4,'is a type of',type(num4))
num5 = 6.6
print(num5,'is a type of',type(num5))
num6 =int(num5)
print(num6,'is a type of',type(num6))
num7 = float(num6)
print(num7,'is a type of',type(num7))
num8 = complex(num5,num6)
print(num8,'is a type of',type(num8))


#list
lst =[10,15,20,25,30,35]
print(lst,'is a type of',type(lst))
print(lst[5])

#tuples
point =(4,5)
print(point[0],'is a type of',type(point))

#dictonaires key value pair
dic ={'India':'New Delhi','France':'Paris','Italy':'Rome'}
print(dic,'is a type of',type(dic))

#set set() is called empty set {}
# value = set()
value = ('poo','lily','rose','lily','jasmine','rose','sunflower','sunflower')
value2 = set(value)
print(value2,'is a type off',type(value2))


#Input
# input will act as a function if we use input it will ask the question
# and we want to asign the input value to other variable and we want to print 

# full_name = input("Whats your name : ")
# print("Hello " + full_name)

# height = float(input("Whats your height :"))
# height_inches = "{:.2f}" .format(height/2.54)
# print("I am " +str(height) +"cm")
# print("you are " +height_inches + " inches tall")

# custom = input("what is your name : ")
# print("User Name " + custom)

# email = input("what is your mail id :")
# print("Email " + email)

# phone = input("what is your Phone number :")
# print("ph " +phone)
                              #Operators
#Arithmetic Operators 
a=10
b=5
print(a+b)
print(a-b)
print(a/b)
print(a*b)
a=8.6677
print(round(a))
print(b**2)

c =8.999
d= 256
f =38
print("this is math ceil value" ,math.ceil(c))
print("math floor value",math.floor(c))
print("math fact value",math.factorial(6))
print("math fmod value",math.fmod(88,5))
print(f%2)
# content = dir(math)
# print (content)

# get =input("give any number ")
# result =int(get)
# print(math.log2(result))
# print(math.cos(result))
# print(math.e)

#Assignment Operators
# assign 10 to a
assign = 10
# assign 5 to b
bbb = 5 
# assign the sum of a and b to a
assign += bbb      # a = a + b
print("The value of assign operators",assign)

#Logical Operators
# logical AND
print(True and True)     
print(True and False)    
# logical OR
print(True or False)    
# logical NOT
print(not True)   

#Identify Operators In Python, is and is not are used to check if two values are located on the same part of the memory. Two variables that are equal does not imply that they are identical.
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
print(x1 is not y1) 
print(x2 is y2)  
print(x3 is y3)  


# conditional stmt
pwd_correct = False
if pwd_correct:
    print("logged In")
else:
    print("Incorrect pwd")    

   #  reraliational opeartor
    num =20
   #  print(num > 0)
   #  print(num < 100)
   #  print(num >= 20)
   #  print(num <=10)
   #  print(num == 27)
   #  print(num !=30)
if num%10==0:
    print(str(num) + " is a multiple of 10")
else:
    print(str(num) + " is not a multiple of 10")   

# else if ladder
# ind_score = int(input("Enter the score: "))
# if ind_score >= 350:
#     print("Ind will win")
# elif ind_score >= 250:
#     print("Ind might win")
# elif ind_score >=150:
#     print("Aus might win")
# else:
#     print("Aus will win")  

# neasted if
#logical operators -and or not

# compare = int(input(" Enter any number:"))  
# if compare > 99 and compare <1000:
#      # 99 < num < 1000
#      if compare % 2==0:
#       print(str(compare) + " is a three digit even number")
# else:
#     print(str(compare)+ " is not a three digit even number")  


#or statement
demo = "Sree" 
if demo[0] == 'S' or demo[0] == "s":
    print("The name starts with s") 

#split and join in string 
str_in ="abc efg hij klmop"
split_list = str_in.split(' ')
print(split_list)
str_join = ','.join(split_list)
print(str_join)

n =5
ar =[2]*n
print(ar)

arr =[[1,2,3],[4,5,6],[7,8,9]]
print("Element at [1][0]=",arr[0][2])
for _ in arr:
    for i in _:
        print(i,end=" ")
        print()
# arr[1].insert(2,12)
# arr.insert(2,[10,11,12])
# arr[1][2]=16
new_arr =[13,14,15]
arr[1]=new_arr
del(arr[1][2])
del(arr[1])
print("inserted array")
for _ in arr:
  for i in _: 
      print(i,end=" ")   
      print()

