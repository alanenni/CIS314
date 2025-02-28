import random
import secrets

randlistPRNG = []
x=0
while x < 10:
    randomint = random.randint(1, 16)
    randlistPRNG.append(randomint)
    x+=1
print("PRNG list -> ",randlistPRNG)


randlistTRNG = []
t= 0
while t < 10:
    rsi = secrets.choice(range(1,17))
    randlistTRNG.append(rsi)
    t+=1
print("TRNG list -> ",randlistTRNG)

def count(randlist):
    countD = {}
    for num in randlist:
        if num in countD:
            countD[num] +=1
        else:
            countD[num] = 1 
    return countD

prngC = count(randlistPRNG)
trngC = count(randlistTRNG)

print(prngC)
print(trngC)
