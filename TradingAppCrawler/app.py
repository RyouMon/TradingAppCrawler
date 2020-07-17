#!/usr/bin/env python
# -*- coding: utf-8 -*-


class DuApp:
    """
    locating ui in du app.
    """
    @property
    def package_name(self):
        """
        application package name
        :return: string
        """
        return 'com.shizhuang.duapp'

    @property
    def rmb_in_order_list(self):
        return {
            'text': "¥"
        }

    @property
    def user_btn(self):
        """
        button to user page
        :return: dict
        """
        return {
            'resource_id': 'com.shizhuang.duapp:id/rbtn_user'
        }

    @property
    def seller_center(self):
        """
        button to seller center
        :return: dict
        """
        return {
            'resource_id': 'com.shizhuang.duapp:id/sellerInfoUp'
        }

    @property
    def trade_success_num(self):
        """
        number(string) of successful order.
        :return: dict
        """
        return {
            'resource_id': 'com.shizhuang.duapp:id/tvTradeSuccessNum'
        }

    @property
    def trade_failed_num(self):
        """
        number(string) of failed order.
        :return: dict
        """
        return {
            'resource_id': 'com.shizhuang.duapp:id/tvTradeFailedNum'
        }

    @property
    def product_name_in_order_detail(self):
        """
        name of product
        :return: dict
        """
        return {
            'resource_id': 'com.shizhuang.duapp:id/tv_product_name'
        }

    @property
    def price_in_order_detail(self):
        """
        price in order detail.
        :return: dict
        """
        return {
            'resource_id': 'com.shizhuang.duapp:id/tv_price'
        }

    @property
    def size_and_quantity_in_order_detail(self):
        """
        size and quantity in order detail.
        :return: dict
        """
        return {
            'resource_id': 'com.shizhuang.duapp:id/tvSizeAndNum'
        }

    @property
    def anticipate_income_in_order_detail(self):
        """
        anticipate income in order detail.
        :return: dict
        """
        return {
            'resource_id': 'com.shizhuang.duapp:id/tvSum'
        }

    @property
    def _order_desc_index(self):
        return {
            'order_id': 1,
            'trade_id': 2,
            'create_time': 3,
        }

    def order_desc_value_in_order_detail(self, kw):
        """
        get order description in order detail.
        :param kw: support following resource_id: order_id, trade_id, create_time
        :return: dict, int
        """
        return {
            'resource_id': 'com.shizhuang.duapp:id/tvOrderDesc',
        }, self._order_desc_index[kw]

    def order_desc_title_in_order_detail(self, kw):
        """
        get order description in order detail.
        :param kw: support following resource_id: order_id, trade_id, create_time
        :return: dict, int
        """
        return {
            'resource_id': 'com.shizhuang.duapp:id/tvOrderTitle',
        }, self._order_desc_index[kw]

    @property
    def page_title_of_order_detail(self):
        return {
            'text': '订单详情'
        }

    @property
    def page_title_of_order_list(self):
        return {
            'text': '我的出售'
        }

    @property
    def _fee_index(self):
        return {
            'technical_fee': 0,
            'transfer_fee': 1,
            'inspection_fee': 2,
            'identification_fee': 3,
            'packing_service_fee': 4,
        }

    def fee_value_in_order_detail(self, kw):
        """
        get fee information in order detail.
        :param kw: support following resource_id:
                   technical_fee, transfer_fee, inspection_fee, identification_fee, packing_service_fee
        :return: dict, int
        """
        return {
            'resource_id': 'com.shizhuang.duapp:id/tvItemValue'
        }, self._fee_index[kw]

    def fee_title_in_order_detail(self, kw):
        """
        get fee name in order detail.
        :param kw: support following resource_id:
                   technical_fee, transfer_fee, inspection_fee, identification_fee, packing_service_fee
        :return: dict, int
        """
        return {
            'resource_id': 'com.shizhuang.duapp:id/tvItemTitle'
        }, self._fee_index[kw]

    @property
    def remark_in_order_detail(self):
        """
        remark in order detail.
        :return: dict
        """
        return {
            'resource_id': 'com.shizhuang.duapp:id/tv_remark_content'
        }

    @property
    def page_load_more(self):
        """
        page load more ui.
        :return: dict
        """
        return {
            'resource_id': 'com.shizhuang.duapp:id/tvLoadMore'
        }
