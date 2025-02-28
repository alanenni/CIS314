
#while loop (for loop in java equivalent)
# x = 1 
# while x <= 10:
#     x += 1 
    # if x == 5:
    #     break  #can also use continue to skip ahead
    # print(x)


#iterables and iterators 
food = ["steak", "potatoes", "beans", "broccoli"]
print(type(food))
food = iter(food)
print(type(food))
print(next(food))
print(next(food))
print(next(food))
print(next(food))

#iter() converts object to an iterator, if possible 
#next() iterates through the object

def it(ob):
    try:
        iter(ob)
        return True
    except TypeError:
        return False
    
    #driver code
for i in [34, [4,5], (4,5), {"a:":4}, "dsdf", 4.5]:
    print(i, "is itereable :",it(i))