#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uiautomator2


class Connector:
    def __init__(self, platform, address):
        self.platform = platform
        self.address = address

    def connect(self):
        if self.platform == 'android':
            return uiautomator2.connect(self.address)