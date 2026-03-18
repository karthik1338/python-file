#sample
name = ""
while name != "joe": 
    name = input("Enter the name ")

print("heloo joe")
#continue
name = ""
while True: 
    name = input("Enter the name ")
    if name != "joe":
        continue
    break

print("heloo joe")
#break
name = ""
while True: 
    name = input("Enter the name ")
    if name == "joe":
        break
    
print("heloo joe")