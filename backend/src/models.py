from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, ForeignKey,CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]
    role: Mapped[str]

    stores = relationship("Store", back_populates="owner")
    points = relationship("UserPoint", back_populates="user")

class Store(db.Model):
    __tablename__ = "stores"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    nombre: Mapped[str]
    direccion: Mapped[str]
    activo: Mapped[bool]
    fecha_de_pago: Mapped[Date]

    owner = relationship("User", back_populates="stores")
    menus = relationship("Menu", back_populates="store")
    categories = relationship("StoreCategory", back_populates="store")
    images = relationship("Image", back_populates="store")
    points = relationship("UserPoint", back_populates="store")

class StoreCategory(db.Model):
    __tablename__ = "storecategories"

    id: Mapped[int] = mapped_column(primary_key=True)
    store_id: Mapped[int] = mapped_column(ForeignKey("stores.id"))
    name: Mapped[str]
    description: Mapped[str]

    store = relationship("Store", back_populates="categories")

class Menu(db.Model):
    __tablename__ = "menus"

    id: Mapped[int] = mapped_column(primary_key=True)
    store_id: Mapped[int] = mapped_column(ForeignKey("stores.id"))
    category: Mapped[str]
    description: Mapped[str]

    store = relationship("Store", back_populates="menus")
    products = relationship("Product", back_populates="menu")

class Product(db.Model):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    menu_id: Mapped[int] = mapped_column(ForeignKey("menus.id"))
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[str]
    image: Mapped[str]

    menu = relationship("Menu", back_populates="products")

class Image(db.Model):
    __tablename__ = "imagenes"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    store_id: Mapped[int] = mapped_column(ForeignKey("stores.id"))
    name: Mapped[str]
    type: Mapped[str]
    url: Mapped[str]
    position: Mapped[int]

    product = relationship("Product", back_populates="images")
    store = relationship("Store", back_populates="images")

class UserPoint(db.Model):
    __tablename__ = "userpoints"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    store_id: Mapped[int] = mapped_column(ForeignKey("stores.id"))
    description: Mapped[str]

    user = relationship("User", back_populates="points")
    store = relationship("Store", back_populates="points")