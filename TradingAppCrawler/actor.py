#!/usr/bin/env python
# -*- coding: utf-8 -*-
from uiautomator2.exceptions import UiObjectNotFoundError


class Actor:
    """
    An actor for Android, interactive with Android device
    """
    def __init__(self, device):
        self.device = device

    def back(self):
        """
        press back button.
        :return boolean
        """
        return self.device.press('back')

    def wait_text(self, text, timeout=1):
        """
        wait until text appear, return boolean.
        :param text: str
        :param timeout: int or float, default 1.
        :return: boolean
        """
        return self.device(text=text).wait(timeout=timeout)

    def wait_text_gone(self, text, timeout=1):
        """
        wait until text gone, return boolean.
        :param text: str
        :param timeout: int or float, default 1.
        :return: boolean
        """
        return self.device(text=text).wait_gone(timeout=timeout)

    def wait_ui_gone_by_resource_id(self, resource_id, timeout=1):
        return self.device(resourceId=resource_id).wait_gone(timeout=timeout)

    def click_by_resource_id(self, resource_id, instance=None):
        """
        click an UI object by resource id.
        :param resource_id: resource id
        :param instance: int
        :return: boolean
        """
        return self.device(resourceId=resource_id, instance=instance).click()

    def click_by_text(self, text, instance=0):
        """
        click an UI object by text
        :param text: str
        :param instance: int, default 0.
        :return: boolean
        """
        return self.device(text=text, instance=instance).click()

    def drag_ui_to_ui_by_text(self, text1, instance, text2, duration=0.5):
        """
        drag an UI to another UI in duration second.
        :param text1: text in UI 1
        :param instance: int
        :param text2: text in UI 2
        :param duration: int or float, default 0.5
        :return: boolean
        """
        return self.device(text=text1, instance=instance).drag_to(text=text2, duration=duration)

    def open_app(self, package_name, **kwargs):
        """
        open application by package name.
        :param package_name: package name
        :param kwargs:
        :return: boolean
        """
        return self.device.session(package_name, **kwargs)

    def fling_to_end(self, *args, **kwargs):
        """
        fling current page to end
        :param args:
        :param kwargs:
        :return: boolean
        """
        self.device(scrollable=True).fling.toEnd(*args, **kwargs)

    def fling_to_beginning(self, *args, **kwargs):
        """
        fling current page to beginning
        :param args:
        :param kwargs:
        :return: boolean
        """
        return self.device(scrollable=True).fling.toBeginning(*args, **kwargs)

    def scroll_to_end(self):
        """
        if current screen exist scrollable UI, scroll it to end.
        :return boolean
        """
        return self.device(scrollable=True).scroll.toEnd()

    def scroll_to_beginning(self):
        """
        if current screen exist scrollable UI, scroll it to top.
        :return boolean
        """
        return self.device(scrollable=True).scroll.toBeginning()

    def get_text_by_resource_id(self, resource_id, instance=None, timeout=0.5):
        """
        get text of nth UI instance by resource id.
        :param resource_id: resource id
        :param instance: int
        :param timeout: int or float, default 0.5.
        :return: if UI object is found, return str, else return "".
        """
        try:
            return self.device(resourceId=resource_id, instance=instance).get_text(timeout=timeout)
        except UiObjectNotFoundError:
            return ""
