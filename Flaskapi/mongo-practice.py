import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
#connect to mongodb 

uri = "mongodb+srv://frandy:k25i04r682a@mycluster.awoytoc.mongodb.net/?retryWrites=true&w=majority&appName=MyCluster"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# put the value in the database
db = client.website # 選擇操作 test database
collection=db.users # 選擇操作 users 集合

#把資料新增到集合中
# try:
#     result = collection.insert_one({
#         "name": "test",
#         "email": "test@gmail.com",
#         "password": "k25i04r682a",
#         "level": 1
#     })
#     print("Insert successfully")
#     print(result.inserted_id)
#     result = collection.insert_many([{
#         "name": "test1",
#         "email": "test1@gmail.com",
#         "password": "k25i04r682a",
#         "level": 5
#     },
#     {
#         "name": "test2",
#         "email": "test2@gmail.com",
#         "password": "k25i04r682a",
#         "level": 5
#     }])
#     print("Insert successfully")
#     print(result.inserted_ids)
# except Exception as e:
#     print(e)

#取得集合中的第一筆文件資料
# data = collection.find_one(
#     ObjectId("66a6196b49da83c6620b617c")
# )
# print(data)
#取得文件資料中的欄位
# print(data["_id"])
# print(data["email"])

#一次取得多筆資料
# cursor = collection.find()
# print(cursor)
# for doc in cursor:
#     print(doc["name"])

#更新集合中的一筆文件資料
# result = collection.update_one({
#     "email" :"frandy@gmail.com"
# }, {
#     "$set": {
#         "long" : 23
#     }
# })
# print("符合條件的文件數量: " , result.matched_count)
# print("實際更新的文件數量: ", result.modified_count)

# result = collection.update_one({
#     "email" :"frandy@gmail.com"
# }, {
#     "$unset": {
#         "long" : 23
#     }
# })
# print("符合條件的文件數量: " , result.matched_count)
# print("實際刪除的文件數量: ", result.modified_count)

# result = collection.update_one({
#     "email" :"frandy@gmail.com"
# }, {
#     "$inc": {
#         "level" : 2
#     }
# })
# print("符合條件的文件數量: " , result.matched_count)
# print("實際加的文件數量: ", result.modified_count)

# result = collection.update_one({
#     "email" :"frandy@gmail.com"
# }, {
#     "$mul": {
#         "level" : 0.5
#     }
# })
# print("符合條件的文件數量: " , result.matched_count)
# print("實際乘的文件數量: ", result.modified_count)

#更新集合中的多筆文件資料
# result=collection.update_many({
#     "level": 2
# }, {
#     "$set": {
#         "level":4
#     }
# })
# print("符合條件的文件數量: " , result.matched_count)
# print("實際乘的文件數量: ", result.modified_count)

#刪除集合中的一筆文件資料
# result = collection.delete_one({
#     "email": "test@gmail.com"
# })
# print("刪除符合條件的文件數量: " , result.deleted_count)

# #刪除集合中的多筆文件資料
# result = collection.delete_many({
#     "level": 5
# })
# print("刪除符合條件的文件數量: " , result.deleted_count)

# 篩選集合中的文件資料
doc = collection.find_one({
    "email": "frandy@gmail.com"
})
print(f"取得的資料的名字欄位:", doc["name"])

#復合篩選條件
doc = collection.find_one({
    "$and" : [
        {"email": "frandy@gmail.com"},
        {"password": "test"}
    ]
})
print("取得的資料" , doc)

#篩選結果排序
cur = collection.find({
    "$or": [
        {"email": "frandy@gmail.com"},
        {"level": 1}
    ]
}, sort=[
    ("level", pymongo.ASCENDING)
])
for doc in cur:
    print(doc)