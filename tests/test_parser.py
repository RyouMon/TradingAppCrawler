#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import json
from TradingAppCrawler.parser import DuParser, DATETIME_FORMAT


class DuParserTest(unittest.TestCase):
    def setUp(self):
        with open('data/test_parser/example.json', encoding='utf-8') as f:
            self.parser = DuParser()
            self.parser.data = json.load(f)

    def test_should_return_str(self):
        self.assertEqual('2020-05-02 22:48:46', self.parser._get_create_time().strftime(DATETIME_FORMAT))
        self.assertEqual('212005022249072224212359', self.parser._get_trade_id())
        self.assertEqual('Supreme FW19 Week 1 Shoulder Bag 单肩包斜挎包 黑色', self.parser._get_product_name())
        self.assertEqual('交易成功', self.parser._get_status_name())
        self.assertEqual('均码', self.parser._get_size_name())
        self.assertEqual('5/3_2_8_赵然', self.parser._get_remarks())

    def test_should_return_float(self):
        self.assertEqual(480.41, self.parser._get_income())
        self.assertEqual(35.0, self.parser._get_technical_fee())
        self.assertEqual(5.59, self.parser._get_transfer_fee())
        self.assertEqual(10.0, self.parser._get_inspection_fee())
        self.assertEqual(18.0, self.parser._get_identification_fee())
        self.assertEqual(10.0, self.parser._get_packing_service_fee())

    def test_should_return_int(self):
        self.assertEqual(110100646395192604, self.parser._get_order_id())
        self.assertEqual(1, self.parser._get_quantity())
