#WAP to create a list of number in the specified range in particular steps. Reverse the list and prints its values
n = int(input('Enter the size of list : '))
list1 = []
for i in range(0,n):
    a = int(input())
    list1.append(a)

print(list1)

list2 = list1[::-1]

print(list2)