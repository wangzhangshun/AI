import json

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import requests

app = FastAPI()


# 数据模型
class User(BaseModel):
    id: int
    name: str
    email: str


# 模拟数据库
users = []


# 更新用户信息
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    for index, existing_user in enumerate(users):
        if existing_user.id == user_id:
            users[index] = user
            return user
    raise HTTPException(status_code=404, detail="User not found")


# 获取用户列表
@app.get("/users", response_model=List[User])
def get_users():
    return users


# 创建新用户
@app.post("/users", response_model=User)
def create_user(user: User):
    users.append(user)
    return user


# 删除用户
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, existing_user in enumerate(users):
        if existing_user.id == user_id:
            users.pop(index)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")


# 获取用户列表
@app.get("/weathers")
def get_weathers():
    url = "https://v1.yiketianqi.com/api?unescape=1&version=v91&appid=47284135&appsecret=jlmX3A6s&ext=&cityid=&city="
    res = requests.get(url)
    return res.json()  # 这样页面数据就可以json化了


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
