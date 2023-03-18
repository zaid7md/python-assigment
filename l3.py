#WAP to create a list of numbers in range 1 to 10. Then delete all the even numbers from the list and print thefinal list
list1 = [ ]
for i in range(1 , 11):
    list1.append(i)

print(list1)

for j in list1:
    if(j%2 == 0 ):
        list1.remove(j)

print(list1)
