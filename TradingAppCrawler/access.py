#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from TradingAppCrawler.order import *
from TradingAppCrawler.parser import *


class Access:
    """
    An access layer for database.
    """
    def __init__(self, url, app):
        self.engine = create_engine(url)
        self.session = sessionmaker(bind=self.engine)()
        if app == 'du':
            self.parser = DuParser()

    def drop_db(self):
        """
        drop a database.
        """
        Base.metadata.drop_all(self.engine)

    def init_db(self):
        """
        initialize a database.
        """
        Base.metadata.create_all(self.engine)

    def insert(self, data):
        """
        insert data to database.
        :param data: json data
        """
        try:
            self.parser.data = data
            product = self._create_product()
            status = self._create_status()
            size = self._create_size()
            order = self._create_order(product, size, status)
            for table in product, status, size, order:
                self.session.add(table)
        except Exception as e:
            print(e)
            self.session.rollback()
        else:
            self.session.commit()

    def _create_order(self, product, size, status):
        """
        create a Order object
        :param product: Product object
        :param size: Size object
        :param status: Stats object
        :return: Order object
        """
        kwargs = self.parser.order
        try:
            order = self.session.query(Order).filter(Order.order_id == kwargs['order_id']).one()
        except NoResultFound:
            order = Order(**kwargs)
            order.product = product
            order.size = size
            order.status = status
            return order
        else:
            raise Exception(f'This order already exists: {order}')

    def _create_product(self):
        """
        create a Product object.
        :return: Product object
        """
        kwargs = self.parser.product
        try:
            product = self.session.query(Product).filter(
                Product.title == kwargs['title'],
            ).one()
        except NoResultFound:
            product = Product(**kwargs)
        return product

    def _create_size(self):
        """
        create a Size object.
        :return: Size object
        """
        kwargs = self.parser.size
        try:
            size = self.session.query(Size).filter(Size.name == kwargs['name']).one()
        except NoResultFound:
            size = Size(**kwargs)
        return size

    def _create_status(self):
        """
        create a Status object.
        :return: Status object
        """
        kwargs = self.parser.status
        try:
            status = self.session.query(Status).filter(Status.name == kwargs['name']).one()
        except NoResultFound:
            status = Status(**kwargs)
        return status

    def iter_orders(self):
        """
        create iterator to return all Order objects.
        :return: Order object
        """
        for order in self.session.query(Order):
            yield order

    def count(self):
        return self.session.query(Order).count()
