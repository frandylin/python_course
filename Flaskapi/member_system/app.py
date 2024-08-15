import pymongo
from flask import *
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://frandy:k25i04r682a@mycluster.awoytoc.mongodb.net/?retryWrites=true&w=majority&appName=MyCluster"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.member_system
collection = db.users


app=Flask(
    __name__,
    static_folder="publice", #靜態檔案名稱
    static_url_path="/" #靜態檔案對應網址路徑
)
app.secret_key="frandylin"

#處理路由
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/members")
def member():
    if "name" in session:
        return render_template("member.html")
    else:
        return render_template("index.html")

#/error?meg=錯誤訊息
@app.route("/error")
def error():
    message  = request.args.get("mes", "please contact costumer service")
    return render_template("error.html", message=message)

@app.route("/register", methods=["POST"])
def register():
    #接收前端資料
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    print(name, email, password)
    # 檢查會員集合是否有已存在帳號
    result = collection.find_one({
        "email": email
    })
    if result != None:
        return redirect("/error?mes=The account is already exists")
    # 把資料放進資料庫
    try:
        result = collection.insert_one({
            "name" : name,
            "email" : email,
            "password" : password
        })
        print("Insert successfully")
        return redirect("/")
    except Exception as e:
        print(f"Insert information fail : {e}")

@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]
    collection = db.users
    result = collection.find_one({
        "$and":[
            {"email":email},
            {"password":password}
        ]
    })
    print(f"Member information: {result}")
    if result == None:
        return redirect("/error?mes=email or password  is incorrect")
    session["name"] = result["name"]
    return redirect("/members")

@app.route("/logout")
def logout():
    del session["name"]
    return redirect("/")


app.run(port=3000)
