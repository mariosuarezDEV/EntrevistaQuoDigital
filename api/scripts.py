from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///instance/default.db")

engine = create_engine(DATABASE_URL)
connection = engine.connect()
users = connection.execute(
    text("SELECT id, name, email, registration_date from users")
).fetchall()
for user in users:
    print(user)
connection.close()
