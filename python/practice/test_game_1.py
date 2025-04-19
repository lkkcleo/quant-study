import random
n = random.randint(1,40)
k = -1
print("I am thinking of a number between 1 and 40.")
while k!= n :
    print("Take a guess.")
    k = int(input())
    if k>n:
        print("too big")
    elif k<n :
        print("too small")
print("good")