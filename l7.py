#WAP to remove all the duplicates from list
list1 = []
n = int(input("Enter size : "))
for i in range(0,n):
    a = input()
    list1.append(a)

print(list1)

list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)

print(list2)