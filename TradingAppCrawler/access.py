#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Access:
    """
    An access layer for database.
    """
    def __init__(self, url):
        self.engine = create_engine(url)
        self.session = sessionmaker(bind=self.engine)

    def insert(self, order, product, size, status):
        """
        insert data to database.
        :param order: Order object
        :param product: Product object
        :param size: Size object
        :param status: Status object
        :return: result
        """
        try:
            self.session.add(order)
            self.session.add(product)
            self.session.add(size)
            self.session.add(status)
        except Exception as e:
            print(e)
            self.session.rollback()
        else:
            self.session.commit()

    def get(self):
        pass

    def delete(self):
        pass

