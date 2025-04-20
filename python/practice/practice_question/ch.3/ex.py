#1.can be repetively used
#2.called
#3. def
#4 function create that function while function call use it
#5 1, inf
#6 delete
#7 what the parameter outside the function received ,  yes
#8 null/None
#9 global
#10 null in other language
#11 import that libary
#12 spam.bacon()
#13 use try , except
#14 try will try to run a code , if have error go to except 
import time 
def collatz(n):
    if n%2 == 0 :
        print(n//2 )
        return n //2 
    print (3 *n+1 )
    return 3*n+1 
while True:
    try:
        n = int(input())
        break
    except ValueError:
        print("enter int")

while n!= 1 :
    n = collatz(n)
    time.sleep(0.1)