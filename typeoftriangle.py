"""
classify the triangles
equilateral triangle a = b = c
isosulouse triangle a = b or b = c or c = a
scalar triangle a != b != c
"""
a,b,c = map(int,input().split())

if a==b==c :
    print("Equilateral Triangle")
elif a==b or b==c or c==a:
    print("Isosules Triangle")
else:
    print("Scalar Triangle")
