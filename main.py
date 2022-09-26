import fastapi
import uvicorn
from fastapi import FastAPI

print("hello fastapi")
api = FastAPI()

@api.get("/")
def endpoint():
    return {"msg": "Hello everyone", "another msg": ["hello", "world"]}

uvicorn.run(api, port=9000)


