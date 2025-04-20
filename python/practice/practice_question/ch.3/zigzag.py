import time,sys
import random
indent = 0 
indentincreasing =1
indentmax = 20
star_length =8
try :
    while True:
        print(' '*indent,end='')
        if indentincreasing==1:
            indent+=1
        if indent >indentmax:
            indent = indentmax
            indentincreasing=-1
            star_length =random.randint(1,20)
        if indentincreasing == -1:
            indent-=1
        if indent <0:
            indent = 0
            indentincreasing=1
            indentmax = random.randint(1,30)
            star_length =random.randint(1,20)
        print('*'*star_length,end='')
        print()
        time.sleep(0.01)
except KeyboardInterrupt:
    sys.exit()