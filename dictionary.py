#集合運算
s1={1,2,3}
print(10 in s1)

s1 = {1,2,3,4}
s2 = {4,5,6}

s3 = s1&s2 #交集 ：相同資料
print(s3)

s3=s1|s2 #連集 ：所有資料且不重複
print(s3) 

s3=s1-s2  #差集  :減去重疊部分
print(s3)

s3=s1^s2 #反差集 : 取兩個集合中, 不重疊的部分
print(s3)

s=set("Hello") # 將字串字母拆解成集合 : set(字串)
print("H" in s)


#字典運算

dic = {"apple": "蘋果" ,"bug": "蟲蟲"}
print("apple" in dic)

del dic["apple"] #刪除字典中的鍵值
print(dic)

dic = {x:x*2 for x in [3,4,5]} #從列表的資料產生字典
print(dic)

