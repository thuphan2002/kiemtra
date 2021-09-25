print("Nhap so nguyen duong n: ")
n = int(input())
def tinhtong(n):
    a = 0
    while (n>0):
        a = a + n%10
        n = int(n/10)
    return a
print("Tổng các chữ số của", n, "là: ",tinhtong(n))