#WAP that creates a list of numbers from 1-20 that are either divisible by 2 or divisible by 4
list1 = []
for i in range(21):
    if(i % 4== 0):
        list1.append(i)

print(list1)