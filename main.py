import math

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
print(str1[0:5])
str = "Attachment"
print(str.find("me"))
print(str.replace("me","xy"))
print(str.count("t"))


#numeric type
num1 = 5
print(num1,'is a type of ',type(num1))
num2 = 5.0
print(num2,'is a type of',type(num2))
num3 = 1+2j
print(num3,'is a type of',type(num3))
num4 = num1 < num2
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

#dictonaires
dic ={'ind': 'new delhi','france':'paris','italy':'rome'}
print(dic,'is a type of',type(dic))

#set
value = ('poo','lily','rose','lily','jasmine','rose','sunflower')
value2 = set(dic)
print(value2,'is a type off',type(value2))


