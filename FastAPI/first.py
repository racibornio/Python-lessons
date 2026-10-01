from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message" : "It works!"}


@app.get("/hello/{name}")
def say_hello(name : str, age : int = 0):
    return {"message" : f"Hello {name}. You are {age} years old."}