## Name:
## hw3.py

##### Template for Homework 3, exercises 1 -  ######


# ********** Exercise 1 ********** 
def is_divisible (m,n):
    if (n==0):
        return "Could not divide by 0"
    if (m%n)!= 0:
        x=False
        return (x)
    if (m%n)==0: 
        x=True
        return(x)
		
# Test cases for is_divisible
print (is_divisible(10,5))  # This should return True
print (is_divisible(18,7))  # This should return False
print (is_divisible(42,0))  # What should this return? It should return error

# ********** Exercise 2 ********** 
def equality_check(a,b):
    if (a-b)==0:
        print ('True')
    if abs(a-b)>0:
        print ('False')

# Test cases for not_equal
equality_check(5,5)
equality_check(5,-5)
equality_check(4/2+9*3,1+7*5)
equality_check(4/2+9/3,25/5)

# ********** Exercise 3 ********** 

## 1 - multadd function
import math
def multadd(a,b,c):
    return(a*b+c)
## 2 - Equations
multadd(3,2,7)
multadd(-3,3,5)
multadd(-2,3,7)

# Test Cases
angle_test = multadd(math.cos(math.pi/4),0.5,math.sin(math.pi/4))
print ("sin(pi/4) + cos(pi/4)/2 is:")
print angle_test

ceiling_test=multadd(math.log(12,7),2,math.ceil(276/19))
print ("ceiling(276/19) + 2 log_7(12) is:")
print ceiling_test


# ********** Exercise 4 **********

## 1 - rand_divis_3 function
import math
import random
def rand_divis_3():
    x = random.randint(0, 100)
    print(x)
    return(is_divisible (x,3))
# Test Cases
rand_divis_3()