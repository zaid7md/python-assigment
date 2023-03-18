#WAP to add two matrices (using nested)
rows = int(input('Enter rows : '))
col = int(input("Enter col : ")) 
m1 = []
for i in range(rows):
    a = []
    for j in range(col):
        print("a[%d][%d] : "%(i,j))
        a.append(int(input()))
    m1.append(a)


m2 = []
for i in range(rows):
    b = []
    for j in range(col):
        print("b[%d][%d] : "%(i,j))
        b.append(int(input()))
    m2.append(b)
        
for i in range(rows):
    for j in range(col):
        print(m1[i][j], end = " ")
    print()

print()
for i in range(rows):
    for j in range(col):
        print(m2[i][j], end = " ")
    print()

m3 = []


for i in range(len(m1)):
    for j in range(len(m1[0])):
        m3[i][j] = m1[i][j]+m2[i][j]

for i in range(rows):
    for j in range(col):
        print(m3[i][j], end = " ")
    print()