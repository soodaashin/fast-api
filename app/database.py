from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:sood@localhost/FastAPI"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"



# while True:
    
#     try:
#         conn = psycopg2.connect(host='localhost', database='FastAPI', user ='postgres', password='sood', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection sucessfull")
        
#         break
        
#     except  Exception as error:
#         print("connection failed")
        
#         print("Error", error)
        
#         time.sleep(3)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


