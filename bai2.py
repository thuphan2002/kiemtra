A = [1,1,2,3,5,8,13,21,34,55,88]
B = [1,3,5,4,7,88,66,59,40,54]
print("List A ", A)
print("List B ", B)
# a)
C= list( set (A) & set (B))
print("Các phần tử trùng nhau trong 2 mảng là", C)

# b)
print("Sau khi xóa các phần tử bị trùng nhau:")
D= list( set (A) ^ set (C))
print("Các phần tử list A là :",D)
E= list( set (B) ^ set (C))
print("Các phần tử list B là :",E)