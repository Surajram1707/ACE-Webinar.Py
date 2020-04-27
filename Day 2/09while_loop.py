# Syntax
# while (condition):
#     opeartions
#     increment / decrement

i = 10
while (i >= 0):
    print (i)
    i -= 1     #short-hand notation for i = i-1


num = int(input("Which Multiplication table you want to print? : "))
upto = int (input("Enter the Limit : "))

i=1
while (i <= upto):
    print ("{} * {} = {}".format(num,i,num*i))
    i+=1