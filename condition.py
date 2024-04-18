n1 = int(input("請輸入第一個數字:"))
n2 = int(input("請輸入第二個數字:"))
op = (input("請輸入運算 + - * % :"))
if op == "+":
    print(n1 + n2)
elif op == "-":
    print(n1-n2)
elif op == "*":
    print(n1*n2)
elif op == "%":
    print(n1%n2)
else:
    print("無法計算請重新輸入")