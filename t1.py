import random
file_t1 = open("data.txt","w")
for i in range(100):
    number = random.randint(1,1000)
    file_t1.write(str(number)+"\n")
file_t1.closed()