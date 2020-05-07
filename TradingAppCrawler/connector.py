#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uiautomator2


class Connector:
    """
    负责连接不同的设备
    """
    def __init__(self, platform, address):
        self.platform = platform
        self.address = address

    def connect(self):
        """
        开始连接，返回连接的设备对象
        :return: Device
        """
        if self.platform == 'android':
            return uiautomator2.connect(self.address)