# Point 實體物件的設計： 平面座標上的點
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
#建立第一個實體物件
p1=Point(3,4)
print(p1.x, p1.y)
#建立第二個實體物件
p2=Point(5,6)
print(p2.x, p2.y)

# Fullname 實體物件的設計 : 分開紀錄姓 , 名資料的全名
class FullName :
    def __init__(self,x, y):
        self.first = x
        self.last = y

a1 = FullName("frandy", "lin")
print(a1.first, a1.last)

# point 實體物件的設計 : 平面座標上的點
class Point:
    #屬性
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #定義實體方法
    def show(self):
        print(self.x, self.y)

    def distance(self, targetx, targety):
        return (((self.x-targetx)**2)+ ((self.y-targety)**2))**0.5 

p = Point(1, 2)
p.show()
result = p.distance(11, 12)
print(result)

#File 實體物件的設計
class File:
    # 初始化
    #屬性
    def __init__(self , name):
        self.name = name
        self.file = None #尚未開啟檔案 : 初期是 none
    #實體方法
    def open(self):
        self.file = open(self.name, mode="r", encoding="utf-8")
    def read(self): 
        return self.file.read()
    
f1 = File("data1.txt")
f1.open()
data = f1.read()
print(data)

f2 = File("data2.txt")
f2.open()
data = f2.read()
print(data)
