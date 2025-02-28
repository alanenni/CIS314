#random number generators
#sorting 
#timing code
#assignment

#true number generators (TRNG) uses natural elemtents to get random numbers 

#pseudo-random number generator (PRNG) algorithm based , subject to predictability on a larger scale 

#when implementing, is there a built in module, do you need PRNG or TRNG 

# import random 

# x=0
# while x <100:
#     print(random.randrange(0,10000))  #gives something greater than or equal to 0 and less than 10000, includes the lower but excludes the higher range
#     x+=1

#can use import os 

#random is not cryptographically secure but secrets and os.usrandom() are


#linear congruential generator (LCG): is not cryptographically secure can be reversed 

#blum blum shub (BBS) - is cryptographically secure 
#x[n+1]=(x[n])^2 mod M
#where x[n] is the current/ initial state(positive int)
#M = p*q

#sorting 
#tuples, sets, and dictionaries cannot be sorted 
#tuples nonmodifiable
#sets are 

# x = "breakfast"
# print(sorted(x))  #breaks down breakfast into ["b","r"...] and then alphabetically sorts it 
# y = [1,4,2,7,3]
# y.sort()
# print(y)


#sorting algorithms
#bubble,insertion,merge,quick - standard algorithms
#also timsort and powersort 

#bubble sort - notes on paper 






