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
    product_id = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer)
    size_id = Column(Integer, ForeignKey('size.id'))
    price = Column(Float)
    technical_fee = Column(Float)
    transfer_fee = Column(Float)
    inspection_fee = Column(Float)
    identification_fee = Column(Float)
    packing_service_fee = Column(Float)
    income = Column(Float)
    status_id = Column(Integer, ForeignKey('status.id'))
    remarks = Column(String)

    def as_dict(self):
        return dict(
            create_time=self.create_time,
            order_id=self.order_id,
            trade_id=self.trade_id,
            product=self.product.title,
            quantity=self.quantity,
            size=self.size.name,
            price=self.price,
            technical_fee=self.technical_fee,
            transfer_fee=self.transfer_fee,
            inspection_fee=self.inspection_fee,
            identification_fee=self.identification_fee,
            packing_service_fee=self.packing_service_fee,
            income=self.income,
            status=self.status.name,
            remarks=self.remarks,
        )


class Status(Base):
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True)
    name = Column(String, UniqueConstraint())
    orders = relationship('Order', backref='status')


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    title = Column(String, UniqueConstraint())
    orders = relationship('Order', backref='product')


class Size(Base):
    __tablename__ = 'size'
    id = Column(Integer, primary_key=True)
    name = Column(String, UniqueConstraint())
    orders = relationship('Order', backref='size')


if __name__ == '__main__':
    from sqlalchemy import create_engine
    engine = create_engine('sqlite:///.test.db', echo=True)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
