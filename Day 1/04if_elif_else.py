# Syntax

# if (condition):  -------------  if it rains 
#     statement   -------------       use an umbrella

print ("Question : What is the Capital of India ?\n1) Chennai\n2) Kolkota\n3) New Delhi\n4) Mumbai")

marks = 0
answer = int(input("Enter the Answer : ")) 
if (answer == 3):
    print ("Congrats!")
    marks += 1

print ("Marks = {}".format(marks))

#Synatx 
# if (condition): ----------- if it is raining :
#     statement   -----------     don't water the plants
# else:                       else:                     
#     statement   -----------     water the plants


print ("Question : What is the Capital of India ?\n1) Chennai\n2) Kolkota\n3) New Delhi\n4) Mumbai")

marks = 0
answer = int(input("Enter the Answer : ")) 
if (answer == 3):
    marks = marks + 1
else:
    marks = marks - 1

print ("Marks = {}".format(marks))

# Syntax
# if (condition):     ------------- if it is red :
#     operation       -------------   turn off the engine
# elif (condition):   ------------- elif it is yellow :
#     operation       -------------   turn on the engine
# else:               ------------- else:
#     operation       -------------   you can go

marks = int(input("Enter your Marks : "))

if (marks >= 85):
    print ("Distinction")
elif (marks >= 60 and marks < 85):
    print ("First Class")
elif (marks >= 50 and marks < 60):
    print ("Second Class")
else:
    print ("Re-Appear")
