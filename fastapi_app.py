from fastapi import Body, Depends, FastAPI, HTTPException
from flask import render_template
from sqlalchemy.orm import Session

from database import User, get_db


app = FastAPI()
@app.post("/login")
def login(username: str = Body(...), password: str = Body(...), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username, User.password == password).first()
    if user:
        return render_template("home.html", users=[user])
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")