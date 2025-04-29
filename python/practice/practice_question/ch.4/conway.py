import random,time , copy 
def check(s, a, b):
    c = 0
    for i in range(a - 1, a + 2):
        for j in range(b - 1, b + 2):
            if i == a and j == b:
                continue  
            if 0 <= i < height and 0 <= j < width:
                if s[i][j] == '*':
                    c += 1
    return c 


def change(s):
    s1 = copy.deepcopy(s)
    for i in range(height):
        for j in range(width):
            if check(s, i, j)==3 or (check(s, i, j)==2 and s[i][j]== '#'):
                s1[i][j] = '*'
            else:
                s1[i][j] = ' '
    return s1


def prins(s):
    for i in range(height):
        for i1 in range (width):
            print (s[i][i1],end='')
        print()

def ini(s):
    for i in range(width) :
        for i1 in range(height):
            s[i1][i]=random.choice(choose)
    return s

width = 60 
height =10 
choose = [' ','*']
s = [[' ' for _ in range(width)] for _ in range(height)]
s = ini(s)
prins(s)
while True:
    s = change(s) 
    prins(s)
    time.sleep(0.1)

