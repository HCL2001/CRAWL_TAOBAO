from sqlalchemy import Column, Integer, String, DateTime, Unicode
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# class Link(Base):
#     __tablename__ = "link"
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(255))
#     brand_id = Column(Integer)
#     create_time = Column(DateTime)
#     link = Column(String(1000))
#
#
# class ProductList(Base):
#     __tablename__ = "product_list"
#     id = Column(Integer, primary_key=True)
#     link_id = Column(Integer)
#     brand_id = Column(Integer)
#     report_id = Column(Integer)
#     price = Column(Integer)
#     original_price = Column(Integer)
#     crawl_time = Column(DateTime)
#     status = Column(Integer)
#     total = Column(String(255))
#     name = Column(String)
#     link = Column(String)
#
#
#
# class Report(Base):
#     __tablename__ = "report"
#     id = Column(Integer, primary_key=True)
#     brand_id = Column(Integer)
#     report_id = Column(Integer)
#     success = Column(Integer)
#     failure = Column(Integer)
#     total = Column(Integer)
#     start_crawl = Column(DateTime)
#     end_crawl = Column(DateTime)
#
#
# class Account(Base):
#     __tablename__ = "account"
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     username = Column(String)
#     password = Column(String)
#     token = Column(String)
#
#
# class Setting(Base):
#     __tablename__ = "setting"
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String)
#     quantity = Column(Integer)
#     unit = Column(String)
#     status = Column(Integer)

class Taobao(Base):
    __tablename__ = "taobao"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Unicode(1000))
    price = Column(Integer)
    shop_name = Column(Unicode(1000))
    is_deleted = Column(String(20))