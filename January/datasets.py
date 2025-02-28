#tuple 
#unmodifiable, indexed, ordered (will always be in the same order)

t = ("a", "b", "c", "d")

print(t)
print(t[0])

t += tuple("d") #copies the og tuple then adds a new value "d" to it 
print(t)


#sets
#modifiable, unindexed, unordered

s = {"a", "b", "c", "d"}

print(s)
#print(s[0]) # doesnt work because the 0 changes eveytime it is used; random 
print("a" in s)


#sets 
#can add() and remove()

x = {"a", "b", "c", "d"}
y = {"e", "f", "g"}


print(x)
x.update(y) # adds y to x, you can add multiple elements with update 
print(x)

#remove() makes sure to remove it, if the element is already not there then there's an error(so you know if its there or not)


#discard() ignores it whether it is there or not 

# clear() 

# pop() removes an element if it is the first element it will remove it, the first one can change so wont always remove the same elememtn 


#lists
#modifiable, indexed, ordered

l = ["a", "b", "c", "d"]

print(l)
l.append("e") #adds e to the end 
l.insert(4, "f") #adds mulitple values 
#updating changes the specified value 
l.remove("a") #removes first a 
print(l)
del l[0] #deletes [0]


d = {
    "num": "CIS 314",
    "name": "Advanced Programming",
    "instructor": "Dane Henry", 
    "credits": 3

}

print(d)
print(d["instructor"])