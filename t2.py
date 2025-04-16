with open("data.txt","r") as file:
    lines = file.readlines()
for line in lines:
    number = int(line.strip())
    if number % 2 == 0:
        print("زوج")
    else:
        print("فرد")