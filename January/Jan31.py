import secrets 

x = 0 
while x < 100:
    print(str(secrets.randbits(16)))
    x += 10

