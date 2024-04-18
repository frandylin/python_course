#定義類別 , 與類別屬性 (封裝載類別中的變數與函示)
class IO:
    supportedSrcs =["console", "file"]
    def read(src):
        if src in IO.supportedSrcs:
            print("Read from :", src)
        else:
            print("Not Supported")



#使用類別
print(IO.supportedSrcs)
IO.read("file")
IO.read("frandy")

