#WAP to print index at which a particular value exists.
#If multiple values, print all the indices and count thenumber of time that value is repeated in the list
list1 = []
n = int(input("Enter size : "))
for i in range(0,n):
    a = int(input())
    list1.append(a)

print(list1)

b = int(input("Enter the data whos indice and occurences you want to know : "))
c = 0 
d = 0 
for i in list1 :
    if b == i :
        print("Element present at index %d"%(c))
        d = d+1

    c = c+1
  
print("total occurence of %d in list : %d"%(b,d))
