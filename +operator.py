#Godfrey Gudah
#Python Operators
#Assignment 1

#Arithmetic Operators...
#Comparison Operators
#Logical Operators
#Identity Operators
#Membership operators
#Assignment operators
#Bitwise Operators
print("Operators")
print("Arrithmetic Operators")

#the + Operators Addition
print("The Addition Operator")
x = 5
y = 3

print(x + y)


# the * Operator
print("The * Operator")
x = 5  #initializing x
y = 3  #initializing y
#printing value
print(x * y)

#the // operators
print("The // Operator")
x = 15
y = 5

print(x // y)


#the % Operator
print("The modulus Operator")
z = 10
a = 23

print(a % z)

#the ** (Exponential) operator
print("The ** (Exponential) Operator")
i = 5
o = 2

print ( o ** i)



print("Comparison Operators")
print("The == operator")

l = 0
i = 10

print(x==y)

print("The != Operator")

q = 9
w = 2

print(q != w)

print("The > Operator")

q = 10
s = 3

if q > s:
    print("q is greater than s")

else:
    print("s is greater than q")

print("the < operator")

q = 10
s = 32

if q < s:
    print("q is smaller than s")

else:
    print("q is greater than s")

print("The >= operator")

u = 10
r = 32

if u >= r:
    print("r is smaller than u")

else:
    print("r is greater than u")

print("The <= operator")

q = 10
s = 32

if q <= s:
    print("q is smaller than s")

else:
    print("q is greater than s")

print("The Logical Operators")

print("Logical And")
x = 10 
y = 30

print(x < y and y < x)

print("Logical or")

x = 10 
y = 30

print(x < y or y < x)

print("Logical not")

x = 10 
y = 30

print(not(x < y and x > y))


print("Identity Operators")

print("Is Operator")

x = -1
y = -1

print(x is y)

print("Is not operator")

x = -2 
y = -2

print(x is not y)

print("Membership Operator")
print("in operator")
#returns true if a sequence of values is found
x = ["Skeeper", "Loyaltie"]

print("Skeeper" in x)
print(x)

print("Not in operator")
#returns true if a sequence of values is found
x = ["Skeeper", "Loyaltie"]

print("Skeeper" not in x)
print(x)

print("BITWISE OPERATORS")

exit()