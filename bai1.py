A = [1,1,2,6,8,9,4,5,6,45,34,66,44,37,78]
B = []
C = []
# a)
print("List A ", A)
for num in A:
    if num < 30:
        B.append(num)
print("Các số nhỏ hơn 30 là: ",B)

# b) 
print("Nhập một số n bất kì: ")
x = int(input())
for n in A:
    if n > x:
        C.append(n)
print("Các số lớn hơn số vừa nhập là: ", C)