import uvicorn
from uuid import UUID, uuid4, uuid5
from fastapi import FastAPI, Request, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from app.controllers.Users import Users

app = FastAPI()
users = Users()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:4200",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Item(BaseModel):
    name: str
    address: str

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )

@app.get("/users")
def getAllUsers():
    try:
        return users.getAllUsers()
    except:
        raise HTTPException(status_code=404, detail="result not found")

@app.get("/users/{id}")
def getSpesificUsers(id:str):
    data = users.getSpesificUsers(id)
    if data == False :
        raise HTTPException(status_code=404, detail={"status": 404, "message": "Unknown user"})
    return data

@app.post("/users")
def addUsers(item:Item):
    return users.addUsers(item)

@app.put("/users/{id}")
def updateUsers(id:str, item:Item):
    return users.updateUsers(id, item)

@app.delete("/users/{id}")
def deleteUsers(id:str):
    return users.deleteUsers(id)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3001)