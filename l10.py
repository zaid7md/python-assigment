#WAP to generate in the Fibonacci sequence and store it in the list. Then find the sum of the even-valuedterms
list1 = []
n = int(input("Enter the numbner of terms of fibonnaci series : "))
a = 0  
b = 1   
for i in range(n):
    print(a,end = " ")
    list1.append(a)
    c = a+b
    a = b 
    b = c 

sum = 0 
for i in range(len(list1)):
    sum = sum+list1[i]

print("Sum : %d"%(sum))