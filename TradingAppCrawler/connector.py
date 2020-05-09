#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uiautomator2
import os


def connect(addr, platform='android'):
    """
    connect device, return Device object.
    :param addr: address for device
    :param platform: device platform, 'android' or 'ios'
    :return: Device
    """
    if platform == 'android':
        os.system('adb connect %s' % addr)
        return uiautomator2.connect(addr=addr)
    elif platform == 'ios':
        pass
