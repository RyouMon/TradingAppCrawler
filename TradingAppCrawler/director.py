#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod, ABC


class Director(metaclass=ABCMeta):
    """
    An abstract class for director.
    Direct the Actor object to complete a series of actions.
    """
    def __init__(self, actor, app, access):
        self.actor = actor
        self.access = access

    @abstractmethod
    def enter_seller_center(self):
        pass

    @abstractmethod
    def enter_success_order_list(self):
        pass

    @abstractmethod
    def enter_fail_order_list(self):
        pass

    @abstractmethod
    def enter_and_exit_first_three_orders(self):
        pass

    @abstractmethod
    def enter_and_exit_first_order_three_times(self):
        pass

    @abstractmethod
    def refresh_order_list(self, required, *args, **kwargs):
        pass

    @abstractmethod
    def back_to_top(self, *args, **kwargs):
        pass

    @abstractmethod
    def scroll_up_three_orders(self):
        pass
