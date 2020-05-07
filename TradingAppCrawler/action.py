#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Action:
    """
    完成对设备的基本操作
    """
    def __init__(self, device):
        self.device = device

    def open_app(self, package_name):
        pass

    def refresh(self):
        pass

    def back(self):
        pass

    def click(self):
        pass