#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Parser(metaclass=ABCMeta):
    @property
    def target(self):
        return self.target

    @target.setter
    def target(self, value):
        pass

    @abstractmethod
    def get_create_time(self):
        pass

    @abstractmethod
    def get_order_id(self):
        pass

    @abstractmethod
    def get_trade_id(self):
        pass

    @abstractmethod
    def get_quantity(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_technical_fee(self):
        pass

    @abstractmethod
    def get_transfer_fee(self):
        pass

    @abstractmethod
    def get_inspection_fee(self):
        pass

    @abstractmethod
    def get_identification_fee(self):
        pass

    @abstractmethod
    def get_income(self):
        pass

    @abstractmethod
    def get_express_no(self):
        pass

    @abstractmethod
    def get_status(self):
        pass

    @abstractmethod
    def get_remarks(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_status_name(self):
        pass

    @abstractmethod
    def get_product_name(self):
        pass

    @abstractmethod
    def get_size_name(self):
        pass
