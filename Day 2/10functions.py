# Syntax
# def function_name(args)
#     statements


def add(a,b):           #Function Definition
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def modulus(a,b):
    return a%b

def square(a):
    # print("Hit in square") # You can add more satements in functions too
    return a**2     #a*a

X = int(input("\nEnter X : "))
Y = int(input("Enter Y : "))
print ("X = {} and Y = {}\n".format(X,Y))

print ("{} + {} = {}".format(X,Y,add(X,Y)))             # Function Call
print ("{} - {} = {}".format(X,Y,subtract(X,Y)))
print ("{} * {} = {}".format(X,Y,multiply(X,Y)))
print ("{} / {} = {}".format(X,Y,divide(X,Y)))
print ("{} % {} = {}".format(X,Y,modulus(X,Y)))
print ("{} ** 2 = {}".format(X,square(X)))

