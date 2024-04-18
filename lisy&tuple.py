#有序可變動列表 List
grades=[1,2,3,4,5,6]

grades[0]=55
print(grades)
print(grades[0:4])

grades[1:4]=[] #連續刪除
grades=grades+[7,8] #串接
print(grades) 

length = len(grades) #取得列表長度
print(len)

#巢狀
data = [[1,2,3],[4,5,6]]
print(data[0][0])

data[0][0:2] = [5,5,5]
print(data)

# 有序不可的變動列表
data=(3,4,5)
