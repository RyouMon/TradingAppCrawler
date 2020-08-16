#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uiautomator2
import os

from .actor import *
from .access import Access


def connect_to_device(addr):
    """
    connect to device, return Actor object.
    :param addr: address for device
    :return: Actor object
    """
    os.system('adb connect %s' % addr)
    return Actor(uiautomator2.connect(addr=addr))


def connect_to_database(username):
    """
    connect to database, return Access object
    :param username: string of username
    :return: Access object
    """
    url = f'sqlite:///{username}.db'
    return Access(url)
