#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from TradingAppCrawler.parser import Parser, DuParser


class DuParserTest(unittest.TestCase):
    def setUp(self):
        with open('example/success_tarding_detail.json', encoding='utf-8') as f:
            self.parser = DuParser(f.read())

    def test_should_return_str(self):
        self.assertEqual('110100646395192604', self.parser.get_order_id())
        self.assertEqual('2020-05-02 22:48:46', self.parser.get_create_time())
        self.assertEqual('212005022249072224212359', self.parser.get_trade_id())
        self.assertEqual('Supreme FW19 Week 1 Shoulder Bag 单肩包斜挎包 黑色', self.parser.get_product_name())
        self.assertEqual('SF1021985167016', self.parser.get_express_no())
        self.assertEqual('交易成功', self.parser.get_status_name())
        self.assertEqual('均码', self.parser.get_size_name())
        self.assertEqual('5/3_2_8_赵然', self.parser.get_remarks())

    def test_should_return_float(self):
        self.assertEqual(480.41, self.parser.get_income())
        self.assertEqual(35.0, self.parser.get_technical_fee())
        self.assertEqual(5.59, self.parser.get_transfer_fee())
        self.assertEqual(10.0, self.parser.get_inspection_fee())
        self.assertEqual(18.0, self.parser.get_identification_fee())
        self.assertEqual(10.0, self.parser.get_packing_service_fee())
        self.parser.remarks = '500.45'
        self.assertEqual(500.45, self.parser.get_cost())

    def test_should_return_int(self):
        self.assertEqual(1, self.parser.get_quantity())
        self.parser.remarks = '500'
        self.assertEqual(500, self.parser.get_cost())

    def test_should_return_none(self):
        self.parser.remarks = '5/3_2_8_赵然'
        self.assertEqual(None, self.parser.get_cost())

