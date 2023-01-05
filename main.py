from typing import Union

from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from db.session import engine
from db.deps import get_db
from models import models
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root(db: Session = Depends(get_db)):
    a = db.query(models.User).filter(models.User.id == 3).first()
    print(a)
    print('aa')
    return {"Hello": a}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
