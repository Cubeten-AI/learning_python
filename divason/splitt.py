
with open("students.txt", "r") as f:
    found = False
    
    data = f.readlines()

for line in data:
    data = line.strip().split(",")
    print(data)