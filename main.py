import math
from array import *
import random
# import function as f
import modules.function as f


student = f.check_pass_fail(50)
print('pass or fail',student)

a ="hello World" 
print(a)

# # create a variable
# name = 'Eric Cartman'
# # print the value
# print(name)

# #variables and print()  
# city ="chennai"
# print(city)
# city="coimbatore"
# print(city)

# place ="chennai"
# destination_place ="New Yok"
# place = destination_place
# print(place)

# street = "mission st"
# location = 6
# print("street:",street , "location:",location)

# #data types in python 
# #string type
# str1 = "Hello"
# str2 ="World"
# print(str1[0])
# print(str2[-1])
# print(str1[0:4])
# strr = "Attachment"
# print(strr.find("me"))
# print(strr.replace("me","xy"))
# print(strr.count("t"))


# #numeric type
# num1 = 5
# print(num1,'is a type of ',type(num1))
# num2 = 5.0
# print(num2,'is a type of',type(num2))
# num3 = 1+2j
# print(num3,'is a type of',type(num3))
# num4 = num1 < num2  # True
# print(num4,'is a type of',type(num4))
# num5 = 6.6
# print(num5,'is a type of',type(num5))
# num6 =int(num5)
# print(num6,'is a type of',type(num6))
# num7 = float(num6)
# print(num7,'is a type of',type(num7))
# num8 = complex(num5,num6)
# print(num8,'is a type of',type(num8))

# #Input
# # input will act as a function if we use input it will ask the question
# # and we want to asign the input value to other variable and we want to print 

# # full_name = input("Whats your name : ")
# # print("Hello " + full_name)

# # height = float(input("Whats your height :"))
# # height_inches = "{:.2f}" .format(height/2.54)
# # print("I am " +str(height) +"cm")
# # print("you are " +height_inches + " inches tall")

# # custom = input("what is your name : ")
# # print("User Name " + custom)

# # email = input("what is your mail id :")
# # print("Email " + email)

# # phone = input("what is your Phone number :")
# # print("ph " +phone)

# #split and join in string 
# str_in ="abc efg hij klmop"
# split_list = str_in.split(' ')
# print(split_list)
# str_join = ','.join(split_list)
# print(str_join)

# n =5
# ar =[2]*n
# print(ar)
#  #Operators
# #Arithmetic Operators 
# a=10
# b=5
# print(a+b)
# print(a-b)
# print(a/b)
# print(a*b)
# a=8.6677
# print(round(a))
# print(b**2)

c =8.999
d= 256
f =38
print("this is math ceil value" ,math.ceil(c))
print("math floor value",math.floor(c))
print("math fact value",math.factorial(6))
print("math fmod value",math.fmod(88,5))
# print(f%2)
# # content = dir(math)
# # print (content)

# # get =input("give any number ")
# # result =int(get)
# # print(math.log2(result))
# # print(math.cos(result))
# # print(math.e)

# #Assignment Operators
# # assign 10 to a
# assign = 10
# # assign 5 to b
# bbb = 5 
# # assign the sum of a and b to a
# assign += bbb      # a = a + b
# print("The value of assign operators",assign)

# #Logical Operators
# # logical AND
# print(True and True)     
# print(True and False)    
# # logical OR
# print(True or False)    
# # logical NOT
# print(not True)   

# #Identify Operators In Python, is and is not are used to check if two values are located on the same part of the memory. 
# #Two variables that are equal does not imply that they are identical.
# x1 = 5
# y1 = 5
# x2 = 'Hello'
# y2 = 'Hello'
# x3 = [1,2,3]
# y3 = [1,2,3]
# print(x1 is not y1) 
# print(x2 is y2)  
# print(x3 is y3)  

#list Mutable
listmethod = [10, 15, 20, 25, 30, 35, 'poo']
print(listmethod,'is a type of',type(listmethod))
print(listmethod[5])
print("Before Append:", listmethod)
# using append method
listmethod.append(66)
print("After Append:", listmethod)

#tuples Immutable 
point =(4,5,'gghhh')
print(point[0],'is a type of',type(point))

#dictonaires key value pair
dic ={'India':'New Delhi','France':'Paris','Italy':'Rome'}
print(dic,'is a type of',type(dic))
del dic["Italy"]
print('del dic',dic)
result = dic.popitem() #delt the last item
print('delt the last item',result)

country_capitals = {
  "United States": "New York", 
  "Italy": "Naples" 
}

# print dictionary keys one by one
for country in country_capitals:
    print(country)

print("----------")

# print dictionary values one by one
for country in country_capitals:
    capital = country_capitals[country]
    print(capital)

#set set() is called empty set {}
# value = set()
value = ('poo','lily','rose','lily','jasmine','rose','sunflower','sunflower')
value2 =set(value)
# value2 = set(dic)
print(value2,'is a type off',type(value2))
value2.discard('poo')
print('print the remove value in set',value2)


# conditional stmt
#if else
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

#for loop
values = range(4)
for i in values:
    print('Print the for loop value of i',i)
#2d
arr=[[1,2,3],[4,5,6],[7,8,9]]
print("Element at [1][0]=",arr[1][0])
print('Original Array')
for _ in arr:
    for i in _:
        print(i,end=" ")
    print()
arr.insert(2, [11, 12, 13])
print("Modified Array")
for _ in arr:
    for i in _:
        print(i, end=" ")
    print()
    arr[1].insert(2,20)
    # del(arr[1][2])
print("Modified Inner Array")
for _ in arr:
    for i in _:
        print(i,end=" ")
    print()

# While loop
# while True:
#    input("Press enter to roll the dice")
#    # get a number between 1 to 6
#    num = random.randint(1,6)
#    print("You got",num)
#    option = input("Roll again?(y/n) ")
#    # condition
#    if option == 'n':
#        break

#break statment
i = 1
while i <= 10:
    print('6 * ',(i), '=',6 * i)
    if i >= 5:
        break
    i = i + 1

# print(dir())

# define a class
class Employee:
    # define an attribute
    employee_id = 0

# create two objects of the Employee class
employee1 = Employee()
employee2 = Employee()

# access attributes using employee1
employee1.employeeID = 1001
print(f"Employee ID: {employee1.employeeID}")

# access attributes using employee2
employee2.employeeID = 1002
print(f"Employee ID: {employee2.employeeID}")


# create a class
class Room:
    length = 0.0
    breadth = 0.0
    
    # method to calculate area
    def calculate_area(self):
        print("Area of Room =", self.length * self.breadth)

# create object of Room class
study_room = Room()

# assign values to all the attributes 
study_room.length = 42.5
study_room.breadth = 30.8

# access method inside class
study_room.calculate_area()


class Bike:
    # constructor function    
    def __init__(self, name):
        self.name = name
bike1 = Bike("Mountain Bike")
print('bike1',bike1.name)

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # def __init__(self, a, b):
    #     self.a = a
    #     self.b = b
    #     self.c = 20

    def calculate_perimeter_of_triangle(self):
        result = self.a + self.b + self.c
        return result

triangle1 = Triangle(2, 4, 6)
# triangle2 = Triangle(2, 4)
# print('the triangle is given as:', triangle2.a)
perimeter = triangle1.calculate_perimeter_of_triangle()
print('perimeter of triangle:', perimeter)


#inheritance a child class inherit all the functionalities of parent class 
# this allow us to code reusability.
class Animal:
    name = ""
    print('checking',name)
    def eat(self):
        print("I can eat")
    print(name)
# inherit from Animal
class Dog(Animal):
    def bark(self):
        print("I can bark")

class Cat(Animal):
    def get_grumpy(self):
      print("I am getting grumpy")
    


# create an object of the subclass
labrador = Dog()
labrador.eat()
labrador.bark()

cat1 = Cat()
cat1.get_grumpy()
cat1.eat()

#module
import asyncio
import time


async def task1():

    wait = random.randint(0, 3)
    await asyncio.sleep(wait)
    print("task 1 finished")


async def task2():

    wait = random.randint(0, 3)
    await asyncio.sleep(wait)
    print("task 2 finished")


async def task3():

    wait = random.randint(0, 3)
    await asyncio.sleep(wait)
    print("task 3 finished")


async def main():

    for x in range(2):
        await asyncio.gather(task1(), task2(), task3())
        time.sleep(1)
        print('----------------------------')

t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()

print(f'Total time elapsed: {t2-t1:0.2f} seconds')