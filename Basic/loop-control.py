#break
n = 0
while n < 5:
    if n == 3 :
        break
    print(n)
    n += 1
print("最後的 n ", n)


#continue
n = 0
for i in [1,2,3,4,5,6]:
    if i%2 == 0:
        continue
    print(i)
    n += 1
print("最後的 n ", n)

#else
sum = 0
for n in range(11):
    sum+= n
else:
    print(sum)


#綜合題目：找出整數平方根
n = int(input("請輸入一個正整數:"))
for i in range(n):
    if i*i ==n :
        print(f"正整數平方根 : {i}")
        break
else:
    print("找不到正整數平方根")