sum = 0
for i in range(100,1000):
    if i % 2 == 0:
        sum += i
print(sum)
count = 0
    if sum // 10 == 0:
        count+=1
    if sum // 100 == 0:
        count +=1
    print("кол-во четных = ", count)