from flask import Flask
from flask import request
import json
from flask import redirect
from flask import render_template
from flask import session
app=Flask(
    __name__,
    static_folder="assets", #靜態檔案名稱
    static_url_path="/library" #靜態檔案對應網址路徑
)
app.secret_key="frandylin" #設定 session 的密鑰
#建立路徑 / 對應的處理函示
@app.route("/")
def index(): #用來回應路徑的處理函示
    print("請求方式:", request.method)
    print("通訊協定:", request.scheme)
    print("主機名稱:", request.host)
    print("路徑:", request.path)
    print("完整的網址:", request.url)
    print("瀏覽器和作業系統:", request.headers.get("user-agent"))
    print("語言偏好:", request.headers.get("accept-language"))
    print("引薦網址:", request.headers.get("referrer"))
    language = request.headers.get("accept-language")
    if language.startswith("zh"):
        return redirect("/zh/")
    else:
        return redirect("/en/")

@app.route("/data")
def handledata():
    return "My data."

@app.route("/user/<username>")
def handleuser(username):
    if username == "frandy":
        return "Your jj so big!"
    else:
        return "User not found."
    
# 利用要求字串 (Query String) 提供彈性 :/getSum?min=最小數字&max=最大數字
@app.route("/getSum")
def getSum():
    maxNumber = request.args.get("max", 100) #100為預設值
    maxNumber = int(maxNumber)
    minNumber = request.args.get("min", 1)
    minNumber = int(minNumber)
    result = 0
    for n in range(minNumber, maxNumber + 1):
        result += n 
    return "result:" + str(result)

@app.route("/gofb")
def gofb():
    return redirect("https://www.facebook.com")

@app.route("/zh/")
def index_chinese():
    return json.dumps({
        "招呼語":"哎呦不錯喔",
        "名字":"林jj"
    }, ensure_ascii=False) # 指示不要用 ascii 編碼處理中文

@app.route("/en/")
def index_english():
    return json.dumps({
        "talk":"Hello, Frandy!",
        "name":"lin jj"
    })

@app.route("/templates")
def templates():
    return render_template("index", name="Frandy")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/page")
def page():
    return render_template("page.html")

@app.route("/show")
def show():
    name=request.args.get("n", "")
    return "success " + name

@app.route("/calculate", methods=["POST"])
def calculate():
    #接收 GET 的 query string
    # maxnumber = request.args.get("max", "")
    #接收 POST 的 query string
    maxnumber = request.form["max"]
    maxnumber=int(maxnumber)
    result = 0
    for n in range(1, maxnumber+1):
        result += n
    return render_template("result.html", data=result)

@app.route("/hello")
def hello():
    name = request.args.get("name", "")
    session["username"] = name #session ["欄位明稱"] = 資料
    return "Hello, " + name

@app.route("/talk")
def talk():
    name = session["username"]
    return name + " welcome back ! I remember you!!"



#啟動網站伺服器 , 可透過 port 參數指定
app.run(port=9000)