import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    s = ''.join(random.choice(['H','T'])for _ in range(6))
    if 'HHHHHH'in s or 'TTTTTT' in s :
        numberOfStreaks+=1
    
    # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))