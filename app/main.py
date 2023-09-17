# main.py
from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class User(BaseModel):
    username: str
    password: str

# Replace with your actual user authentication logic
def authenticate_user(user: User):
    # Replace this with your authentication logic (e.g., checking credentials in a database)
    if user.username == "demo" and user.password == "password":
        return True
    return False

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login", response_class=HTMLResponse)
async def login(user: User, request: Request):
    if authenticate_user(user):
        return templates.TemplateResponse("welcome.html", {"request": request, "user": user.username})
    else:
        raise HTTPException(status_code=401, detail="Login failed")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
