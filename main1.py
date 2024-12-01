from fastapi import FastAPI

app=FastAPI()




# def my_decorator(path:str,operation:str):

#     def decorator(func):
#         app.add_api_route(path,func,methods=operation)
#         return func
#     return decorator

# @my_decorator(path="/myCustomRoute",operation=["GET"])
# def cutomroute():
#     return {"message":"this is my custom decorator route"}

# @app.get("/")
# async def root():
#     return {"message":"This is home page route"}

# @app.post("/SignIn")
# async def signIn():
#     return {"message":"This is sign in route"}

# @app.post("/SignUp")
# async def signUp():
#     return {"message":"This is sign up route"}



@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

