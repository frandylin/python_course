import pandas as pd
#建立 Series = 單維度資料
data = pd.Series([1,2,3,4,5])
#Series 操作
print(data)
print("Max:", data.max())
print("Median:", data.median())
data = data*2
print(data)

data=data==2
print(data)

#print (data)

#建立 DataFrame
data=pd.DataFrame({
    "name":["frandy","chloe","jeff"],
    "salary":[3000, 2000, 1000]
})

# 基本 DataFrame 操作
print(data)
# 取得特定欄位
print(data["name"])
#取得特定列
print(data.iloc[0]) #取得第一列

#資料索引
data=pd.Series([5, 4, -3, 2, 1], index=["a", "b", "c", "d", "e"])
print(data)

#觀察資料
print("資料型態:" , data.dtype)
print("資料數量:" , data.size)
print("資料索引:" , data.index)

#取得資料: 根據順序, 根據索引
print(data[0], data[1])
print(["a"],["c"])

#數字運算 : 基本 , 統計 , 順序
print("最大值:" , data.max())
print("總和:" , data.sum())
print("標準差:" , data.std())
print("中位數:" , data.median())
print("最大三個數 & 最小三個數:" , data.nlargest(3) , data.nsmallest(2))

#字串運算 : 基本 , 串接 , 搜尋 ,取代
data=pd.Series(["您好" , "Frandy", "Lin"])

print(data.str.lower()) #全部變小寫
print(data.str.upper()) #全部變大寫
print(data.str.cat(sep="&")) #把字串串在一起, 並可以自訂串接的符號
print(data.str.contains("F")) #判斷每一筆字串是否有包和特定字元
print(data.str.replace("Frandy", "Bigjj"))  
