#pemdas
'''
print (1+1)**1*1/1+1-1
print (1+1/1*(1+1)**1-1)
#(1+1)=2
#2**1=2
#1*2=2
#2/1=2
#2+1=3
#3-1=2
'''
'''
import random

print (random.randint(0,100))
'''
'''
lamp = False
plugged_in = True
burned_out= True

if lamp == plugged_in:
   if lamp == burned_out:
       print("Replace Lamp")
   else:
    print("Replace Lamp")       
else:
    print("plug in Lamp")
'''
'''
age = 18

if age < 18:
    print("mapriso ka!")

else:
    print("pwede na")

    '''
'''
age = 12
   
if (age < 18 and age >0):
        print("mapriso ka!")
elif (age > 17 and age < 60):
        print("pwede na")
elif (age > 59 and age <100):
       print("ayaw na tay!")
else:
    print("invalid age")
'''
from random import randint

ako = input("PILI 5 HAYANG to 0 KULOB:")
c2 = randint (0,5)
c3 = randint (0,5)

hayang = 5
kulob = 0

if ako == 0:
    print("ako-kulob")
elif ako == 5:
    print("ako-hayang")

if c2 == 5:
    print("c2-hayang")
elif c2 == 0:
    print("c2-kulob")

if c3 == 0:
    print("c3-kulob")
elif c3 == 5:
    print("c3-hayang")

if ako == 0 and c2 == 5 and c3 == 0 or ako == 5 and c2 == 0 and c3 == 5 :
   print("YOU WIN")

elif ako == 5 and c2 == 0 and c3 == 5 or ako == 0 and c2 == 5 and c3 == 0:
    print("YOU WIN")

elif ako == 0 and c2 == 5 and c3 == 0 or ako == 5 and c2 == 0 and c3 == 5:
    print("YOU WIN")
else:
    print("LAHI ABAL!!")

 