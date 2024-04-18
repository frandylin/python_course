#使用參數名稱對應
def divide(a1 , a2):
    print(a1/a2)

divide(4, 2)
divide(a1 = 9, a2 = 3)

#無限/不定參數資料 :
def avg(*number):
    sum = 0
    for i in number:
        sum = sum + i
        print(sum/len(number))

avg(1,2,3)