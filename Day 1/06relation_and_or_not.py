a = 3
b = 4
c = 5

print ("Is {} > {} ? ".format(a,b))
print ("Answer : {}".format(a>b))

print ("Is {} < {} ? ".format(b,c))
print ("Answer : {}".format(b<c))

print ("Is {} <= {} ? ".format(b,c))
print ("Answer : {}".format(b<=c))

print ("Is {} >= {} ? ".format(b,c))
print ("Answer : {}".format(b>=c))

print ("Is {} == {} ? ".format(b,c))
print ("Answer : {}".format(b==c))

print ("Is {} != {} ? ".format(b,c))
print ("Answer : {}".format(b!=c))

# AND 
(4==4) and (5==5) #----------- True
(4==4) and (5==8) #----------- False
(4==3) and (5==5) #----------- False
(4==3) and (5==8) #----------- False

# OR
(4==4) or (5==5) #----------- True
(4==4) or (5==8) #----------- True
(4==3) or (5==5) #----------- True
(4==3) or (5==8) #----------- False

# NOT

not 5 #------ False
not 0 #------ True