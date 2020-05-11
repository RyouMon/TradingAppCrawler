#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep


class Actor:
    """
    An actor for Android, interactive with Android device
    """
    def __init__(self, device):
        self.device = device

    def back(self):
        """
        press back button.
        """
        self.device.press('back')

    def wait_text(self, text, timeout=1):
        self.device(text=text).wait(timeout=timeout)

    def wait_text_gone(self, text, timeout=1):
        self.device(text=text).wait_gone(timeout=timeout)

    def click_by_resource_id(self, resource_id):
        """
        click an UI object by resource id.
        :param resource_id: resource id
        """
        self.device(resourceId=resource_id).click()

    def click_by_text(self, text, instance: int):
        self.device(text=text, instance=instance)

    def open_app(self, package_name, **kwargs):
        """
        open application by package name.
        :param package_name: package name
        :param kwargs:
        :return:
        """
        self.device.session(package_name, **kwargs)

    def fling_to_end(self, *args, **kwargs):
        self.device(scrollable=True).fling.toEnd(*args, **kwargs)

    def fling_to_beginning(self, *args, **kwargs):
        self.device(scrollable=True).fling.toBeginning(*args, **kwargs)

    def scroll_to_end(self):
        """
        if current screen exist scrollable UI, scroll it to end.
        """
        self.device(scrollable=True).scroll.toEnd()

    def scroll_to_top(self):
        """
        if current screen exist scrollable UI, scroll it to top.
        """
        self.device(scrollable=True).scroll.toBeginning()

    def get_text_by_resource_id(self, resource_id, timeout=2):
        self.device(resourceId=resource_id).get_text(timeout=timeout)
