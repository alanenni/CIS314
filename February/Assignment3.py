colors = ("blue", "yellow", "red", "orange", "pink", "purple", "black", "brown", "white", "clear") #creates a tuple of colors 
reversedColors = tuple(reversed(colors)) # creates a tuple of Colors reversed 
print(colors)
print(reversedColors)
print("The third element of the tuple Colors is", colors[2])
print("The third element of the tuple reversedColors is", reversedColors[2])
colorsRan = set(colors) # converts the tuple colors into a set in order to rendomize the items within 
colorsRan = tuple(colors) # converts the set colors back into a tuple 
print("The tuple colors randomized: ", colorsRan)

colors11 = colors + ("gold", )
print(colors11)

