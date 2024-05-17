from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import SQLALSCHEMY_DATABASE_URL, Base, User


engine = create_engine(SQLALSCHEMY_DATABASE_URL)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind = engine)
db = SessionLocal()

test_users = [
    {"username": "admin", "password": "admin"},
    {"username": "test", "password": "test"}
]

for user_data in test_users:
    user = User(**user_data)
    db.add(user)
db.commit()
db.close()
