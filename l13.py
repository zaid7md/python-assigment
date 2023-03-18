#WAP to calculate distance between two p
point1 = []
point2 = []
print("Point 1 coord")
for i in range(3):
    a = int(input())
    point1.append(a)

print("Point 2 coord")
for i in range(3):
    b = int(input())
    point2.append(b)

print(point1)
print(point2)

d = 0 
for i in range(3):
    d = d + (point1[i] - point2[i])**2

print('Distance = ',d**0.5)