#WAP to find the median of a list of numb
list1 = [12 ,212 , 1 , 0 , 121 , 65 , 32]
list1.sort()
print(list1)

if len(list1)%2 == 0:
   f1 = list1[len(list1) // 2]
   f2 = list1[len(list1) // 2 - 1]
   median = (f1 + f2) / 2
else:
   median = list1[len(list1) // 2]

   
print("Median : ",median)