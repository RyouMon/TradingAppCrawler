#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from datetime import datetime
from abc import ABCMeta, abstractmethod


DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'


class Parser(metaclass=ABCMeta):
    """
    Provide Table construction parameters for Access class
    """
    def ___init__(self, target=None):
        self.target = target

    @property
    @abstractmethod
    def order(self):
        pass

    @property
    @abstractmethod
    def size(self):
        pass

    @property
    @abstractmethod
    def product(self):
        pass

    @property
    @abstractmethod
    def status(self):
        pass

    @abstractmethod
    def _get_create_time(self):
        pass

    @abstractmethod
    def _get_order_id(self):
        pass

    @abstractmethod
    def _get_trade_id(self):
        pass

    @abstractmethod
    def _get_quantity(self):
        pass

    @abstractmethod
    def _get_price(self):
        pass

    @abstractmethod
    def _get_technical_fee(self):
        pass

    @abstractmethod
    def _get_transfer_fee(self):
        pass

    @abstractmethod
    def _get_inspection_fee(self):
        pass

    @abstractmethod
    def _get_identification_fee(self):
        pass

    @abstractmethod
    def _get_packing_service_fee(self):
        pass

    @abstractmethod
    def _get_income(self):
        pass

    @abstractmethod
    def _get_remarks(self):
        pass

    @abstractmethod
    def _get_status_name(self):
        pass

    @abstractmethod
    def _get_product_name(self):
        pass

    @abstractmethod
    def _get_size_name(self):
        pass


class DuParser(Parser):
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def order(self):
        return dict(
            create_time=self._get_create_time(),
            order_id=self._get_order_id(),
            trade_id=self._get_trade_id(),
            quantity=self._get_quantity(),
            price=self._get_price(),
            technical_fee=self._get_technical_fee(),
            transfer_fee=self._get_transfer_fee(),
            inspection_fee=self._get_inspection_fee(),
            identification_fee=self._get_identification_fee(),
            packing_service_fee=self._get_packing_service_fee(),
            income=self._get_income(),
            remarks=self._get_remarks(),
        )

    @property
    def size(self):
        return dict(
            name=self._get_size_name()
        )

    @property
    def product(self):
        return dict(
            title=self._get_product_name()
        )

    @property
    def status(self):
        return dict(
            name=self._get_status_name()
        )

    def _get_create_time(self):
        """
        return create time
        :return: datetime
        """
        return datetime.strptime(self._data['create_time'], DATETIME_FORMAT)

    def _get_order_id(self):
        """
        return order id
        :return: int
        """
        return int(self._data['order_id'])

    def _get_trade_id(self):
        """
        return trade id
        :return: string
        """
        return self._data['trade_id']

    def _get_quantity(self):
        """
        return quantity
        :return: int
        """
        return 1

    def _get_price(self):
        """
        return price
        :return: float
        """
        return float(self._data['price'])

    def _get_technical_fee(self):
        """
        return technical fee
        :return: float
        """
        return float(self._data['technical_fee'])

    def _get_transfer_fee(self):
        """
        return transfer fee
        :return: float
        """
        return float(self._data['transfer_fee'])

    def _get_inspection_fee(self):
        """
        return inspection fee
        :return: float
        """
        return float(self._data['inspection_fee'])

    def _get_identification_fee(self):
        """
        return identification fee
        :return: float
        """
        return float(self._data['identification_fee'])

    def _get_packing_service_fee(self):
        """
        return packing service fee
        :return: float
        """
        return float(self._data['packing_service_fee'])

    def _get_income(self):
        """
        return income
        :return: float
        """
        return float(self._data['income'])

    def _get_remarks(self):
        """
        return remarks
        :return: string
        """
        return self._data['remarks']

    def _get_status_name(self):
        """
        return status name
        :return: string
        """
        return self._data['status']

    def _get_product_name(self):
        """
        return product name
        :return: string
        """
        return self._data['product']

    def _get_size_name(self):
        """
        return size name
        :return: string
        """
        return self._data['size']
