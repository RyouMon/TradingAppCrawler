#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from datetime import datetime
from abc import ABCMeta, abstractmethod


class Parser(metaclass=ABCMeta):
    def __init__(self, target=None):
        self.target = target

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
    def get_packing_service_fee(self):
        pass

    @abstractmethod
    def get_income(self):
        pass

    @abstractmethod
    def get_express_no(self):
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
    def get_identify_no(self):
        pass

    @abstractmethod
    def get_size_name(self):
        pass


class DuParser(Parser):
    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        if value:
            self._target = json.loads(value).get('data')
        else:
            self._target = None

    def get_create_time(self):
        datetime_str = self.target['extraInfoList'][1]['desc']
        return datetime_str

    def get_order_id(self):
        return self.target['extraInfoList'][0]['desc']

    def get_trade_id(self):
        return self.target['extraInfoList'][2]['desc']

    def get_quantity(self):
        return 1

    def get_price(self):
        return self.target['skuInfo']['skuPrice']/100

    def get_technical_fee(self):
        return self.target['feeInfo']['feeList'][0]['actualFee']/100

    def get_transfer_fee(self):
        return self.target['feeInfo']['feeList'][1]['actualFee']/100

    def get_inspection_fee(self):
        return self.target['feeInfo']['feeList'][2]['actualFee']/100

    def get_identification_fee(self):
        return self.target['feeInfo']['feeList'][3]['actualFee']/100

    def get_packing_service_fee(self):
        return self.target['feeInfo']['feeList'][4]['actualFee']/100

    def get_income(self):
        return self.target['feeInfo']['amountSum']/100

    def get_express_no(self):
        return self.target['trackInfo']['expressNo']

    def get_remarks(self):
        self.remarks = self.target['remark']
        return self.remarks

    def get_cost(self):
        if self.remarks:
            try:
                cost = eval(self.remarks)
            except SyntaxError:
                cost = None
            return cost
        else:
            return None

    def get_status_name(self):
        return self.target['statusInfo']['statusDesc']

    def get_product_name(self):
        return self.target['skuInfo']['skuTitle']

    def get_identify_no(self):
        return self.target['skuInfo']['articleNumber']

    def get_size_name(self):
        return self.target['skuInfo']['skuProp']
