# Put your code here
import math     #math module for getting pi value

#get the number of iterations from the user
n=int(input())
res=0   #result is stored here
ic=1    #denominator value

#loop for iterations
for i in range(1,n+1):
    if(i%2!=0):     #if it is odd term
        res+=1/ic
      
    else:           #if it is even term
        res-=1/ic
  
    ic+=2           #increment ic by 2 after each term

res*=4              #multiply by 4 to get the pi approx value

#print the result and the actual pi value
print(res, math.pi)
