in_data = []
in_file = open(r"C:\Users\alanj\Downloads\access.log")
in_data = in_file.readlines()
print(in_data)
print("Number of bot attempts:", in_data.count("BotPoke"))

x = 0
while x < len(in_data):
    if in_data[x].find("BotPoke") >= 0:
        in_data.pop(x)
    else:
        x += 1

out_file = open("parsed_access.log", "w")
out_file.writelines(in_data)
out_file.close()    

print(in_data)
print("Number of bot attempts:", in_data.count("BotPoke"))
print("Number of remaining logs", len(in_data))