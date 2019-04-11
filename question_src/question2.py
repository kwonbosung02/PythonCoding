a, b = input("두 수를 입력하세요 : ").split(",")
a = float(a)
b = float(b)
if b < a : a , b = b , a
b = a
for i in range(10):
    a += b
print('{:0.2f}'.format(a))