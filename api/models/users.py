from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime, timezone


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class UsersModel(db.Model):
    __tablename__ = "users"
    # nombre - email (unico) - fecharegistro
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    registration_date: Mapped[datetime] = mapped_column(
        nullable=False, default=datetime.now(timezone.utc)
    )
