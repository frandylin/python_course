#定義函數
def multiply(a1, a2):
    print(a1*a2)
    value = a1*a2
    return value
result = multiply(1,9) + multiply(2,2)
print(result)


#函式可以用來做程式的包裝: 同樣邏輯可以重複使用
def calculate(max):
    sum = 0 
    for i in range(1, max+1):
        sum = sum + i
    print(sum)


calculate(10)
