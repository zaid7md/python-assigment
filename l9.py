#WAP that creates a list of 10 random integers. Then creates two lists--- Odd list and Even list that has all oddand even values in the list respectively. 
#(Import random )
import random 
list1 = []
for i in range(11):
    a = random.randint(0,100000)
    list1.append(a)

print(list1)

list2 = []
list3 = []
for i in list1:
    if(i%2==0):
        list2.append(i)
    else:
        list3.append(i)

print("Even : ",list2)
print("Odd  : ",list3)