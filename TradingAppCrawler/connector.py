#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uiautomator2
import os


def connect(addr):
    """
    connect device, return Device object.
    :param addr: address for device
    :return: Device
    """
    os.system('adb connect %s' % addr)
    return uiautomator2.connect(addr=addr)
