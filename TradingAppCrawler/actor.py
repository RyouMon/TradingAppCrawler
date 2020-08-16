#!/usr/bin/env python
# -*- coding: utf-8 -*-
from uiautomator2.exceptions import UiObjectNotFoundError


class Actor:
    """
    An access layer for uiautomator2.
    """
    def __init__(self, device):
        self.device = device

    def back(self):
        """
        press back button.
        :return boolean
        """
        return self.device.press('back')

    def click_by(self, method, properties, instance=None, *args, **kwargs):
        """
        click an UI object by properties
        :param method:
        :param properties: dict of ui properties
        :param instance: int, default 0.
        :return: boolean
        """
        return eval(f"self.device({method}={properties}['{method}'], instance={instance}, *{args}, **{kwargs}).click()")

    def drag_ui_to_ui_by(self, method, properties1, properties2, from_instance, duration=0.5):
        """
        drag an UI to another UI in duration second.
        :param method: 
        :param properties1: properties of first ui.
        :param properties2: properties of second ui.
        :param from_instance: int, nth kw of UI 1.
        :param duration: int or float, default 0.5
        :return: boolean
        """
        return eval(f'self.device({method}={properties1}["{method}"], instance={from_instance}).drag_to({method}={properties2}["{method}"], duration={duration})')

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

    def get_ui_by(self, method, properties, instance=None):
        return eval(f"self.device({method}={properties}['{method}'], instance={instance})")

    def get_text_by(self, method, properties, instance=None, timeout=0.5):
        """
        get properties of nth UI kw by resource id.
        :param method:
        :param properties: dict of ui properties
        :param instance: int
        :param timeout: int or float, default 0.5.
        :return: if UI object is found, return str, else return "".
        """
        try:
            return eval(f"self.device({method}={properties}['{method}'], instance={instance}).get_text(timeout={timeout})")
        except UiObjectNotFoundError:
            return ""

    def open_app(self, package_name, **kwargs):
        """
        open application by package name.
        :param package_name: package name
        :param kwargs:
        :return: boolean
        """
        return self.device.session(package_name, **kwargs)

    def scroll_to_end(self, *args, **kwargs):
        """
        if current screen exist scrollable UI, scroll it to end.
        :return boolean
        """
        return self.device(scrollable=True).scroll.toEnd(*args, **kwargs)

    def scroll_to_beginning(self, *args, **kwargs):
        """
        if current screen exist scrollable UI, scroll it to top.
        :return boolean
        """
        return self.device(scrollable=True).scroll.toBeginning(*args, **kwargs)

    def wait_ui_by(self, method, properties, instance=None, timeout=1):
        return eval(f"self.device({method}={properties}['{method}'], instance={instance}).wait(timeout={timeout})")

    def wait_ui_gone_by(self, method, properties, instance=None, timeout=1):
        return eval(f"self.device({method}=properties['{method}'], instance={instance}).wait_gone(timeout={timeout})")
