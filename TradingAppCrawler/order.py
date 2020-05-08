#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, UniqueConstraint
from sqlalchemy import Float, String, DateTime, Integer
from sqlalchemy.orm import relationship


Base = declarative_base()


class Order(Base):
    __tablename__ = 'order'
    create_time = Column(DateTime)
    order_id = Column(Integer, primary_key=True)
    trade_id = Column(String)
    product = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer)
    size = Column(Integer, ForeignKey('size.id'))
    price = Column(Float)
    technical_fee = Column(Float)
    transfer_fee = Column(Float)
    inspection_fee = Column(Float)
    identification_fee = Column(Float)
    income = Column(Float)
    express_no = Column(String)
    status = Column(Integer, ForeignKey('status.id'))

    def as_dict(self):
        return dict(
            create_time=self.create_time,
            order_id=self.order_id,
            trade_id=self.trade_id,
            product=self.product,
            quantity=self.quantity,
            size=self.size,
            price=self.price,
            technical_fee=self.technical_fee,
            transfer_fee=self.transfer_fee,
            inspection_fee=self.inspection_fee,
            identification_fee=self.identification_fee,
            income=self.income,
            express_no=self.express_no,
            status=self.status,
        )


class Status(Base):
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True)
    name = Column(String, UniqueConstraint())
    order = relationship('Order', backref='status')


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    identify_no = Column(String)
    order = relationship('Order', backref='product')


class Size(Base):
    __tablename__ = 'size'
    id = Column(Integer, primary_key=True)
    title = Column(String, UniqueConstraint())


from sqlalchemy import create_engine


engine = create_engine('sqlite:///.test.db', echo=True)
#Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
