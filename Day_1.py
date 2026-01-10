# data type 

# checking the data type 
x = 5 
type(x)


x = "Prajjwol Thapa"
type(x)


x = 3 + 5j       # imaginary numbers
type (x)


# setting the data type 

fruits = ['apple', 'banana']
type (fruits)


x = range(6)
x


x = bool(5)
x


z = -12345455666
type(z)


# type conversion 
x = 1
y = 2.8 
z = 1j 

to_int = int(y)
type(to_int)

to_complex = complex(y)    # we cannot convert complex numbers into another data type.
type(to_complex)


# random number 

import random 

random.randrange(1,20)    # generates the random number between 1 to 20 


# python casting 

x = float(1)
type(x)

x = str(1.23456)
type(x) 

# python functions 

def my_name():
    print("Hello, this is me.")

my_name()
# converting fahrenheit to celcius

def fah_to_cel(fahrenheit):
    return (fahrenheit - 32)* 5/9

fah_to_cel(100)
fah_to_cel(200)


# return values

def get_greeting():
    return "Hello, Good Morning Everybody!"

message = get_greeting()
print(message)

print(get_greeting())      # we can directly return value


# the pass statement 

def my_football_team():
    pass 

print(my_football_team())       # function with no return values returns None.


# python function arguments 

def check_arguments(fname):
    print (fname + " Thapa")

check_arguments("Prajjwol")
check_arguments('Kriti')


# parameters and arguments 

def this_parameter(Lname):              # Lnane is parameter 
    print ('Prajjwol' + Lname)

this_parameter(' Thapa')                # Thapa is argument


# number of arguments 

def no_of_Arguments(fname, mname, lname):          
    print (fname +' ' + mname + ' ' + lname)

no_of_Arguments('Prajjwol', 'Kaji', 'Thapa')


# default parameter values

def default_parameter(name = 'Friend'):        # here friend is the default parameter values
    print('Hello' + ' ', name)

default_parameter('Prajjwol')
default_parameter()


# keyword arguments

def pet_name(dog, dog_name, cat, cat_name):
    print('I have a '+ dog + ' named' + dog_name + ' and' + cat + ' named as' + cat_name)

print(pet_name(dog = 'husky', dog_name=' Khairey', cat=' Persian Cat', cat_name=' Millie.'))