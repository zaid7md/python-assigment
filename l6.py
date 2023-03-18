#WAP that forms a list of first character of every words in another list.
list1 = []
n = int(input("Enter size : "))
for i in range(0,n):
    a = input()
    list1.append(a)

print(list1)

list2 = []
for i in range(len(list1)):
    list2.append(list1[i][0])

print(list2)