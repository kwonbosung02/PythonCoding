a, b = input("두 수를 입력하세요 : ").split(",")
a = int(a)
b = float(b)
print("두 수의 합 : "+str('{:0.2f}'.format(a+b)))
print("두 수의 곱 : "+str('{:0.2f}'.format(a*b)))
print("두 수의 차 : "+str('{:0.2f}'.format(a-b)))
print("a의 타입 : "+str(type(a)))
print("b의 타입 : "+str(type(b)))
