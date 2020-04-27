# Syntax
# for variable in sequence:
#     statements to repeat

print ("\nLoop 1 :")
for i in range (10):
    print(i)

print ("\nLoop 2 :")
for i in range (1,10):
    print(i)

n = 15
print ("\nLoop 3 :")
for i in range (1,n+1,2):
    print(i)


num = int(input("Which Multiplication table you want to print? : "))
upto = int (input("Enter the Limit : "))

for i in range(1,upto+1):
    print("{} * {} = {}".format(num,i,num*i))


# Iterating over a list
list1 = [3,4,5,"A"]

i=0
for var in list1:
    i+=1
    if(var == 5):
        break
    print(var,end="")

