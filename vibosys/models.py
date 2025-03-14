from sqlalchemy import Column, Integer, String, Enum, Text, TIMESTAMP, BigInteger
from sqlalchemy.sql import func
from db import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(100))
    category = Column(Enum("finished", "semi-finished", "raw"))
    description = Column(String(250))
    product_image = Column(Text)
    sku = Column(String(100))
    unit_of_measure = Column(Enum("mtr", "mm", "ltr", "ml", "cm", "mg", "gm", "unit", "pack"))
    lead_time = Column(Integer)
    created_date = Column(TIMESTAMP, server_default=func.now())
    updated_date = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
