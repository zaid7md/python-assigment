#WAP that creates a list of words by combining the words in two individual lists
list1 = []
n = int(input("Enter size : "))
for i in range(0,n):
    a = input()
    list1.append(a)

print(list1)

list2 = []
n = int(input("Enter size : "))
for i in range(0,n):
    a = input()
    list2.append(a)

print(list2)
list3 = []
p = len(list1)
q  = len(list2)

if p == q:
    for i in range(0,q):
        list3.append(list1[i]+list2[i])


print(list3)

