#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Action:
    """
    Base Action.
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

    def click_by_resource_id(self, resource_id):
        pass


class AndroidAction(Action):
    """
    Base actions for Android
    """
    def click_by_resource_id(self, resource_id):
        """
        click an UI object by resource id.
        :param resource_id: resource id
        """
        self.device(resourceId=resource_id).click()

    def back(self):
        """
        press back button.
        """
        self.device.press('back')

    def open_app(self, package_name, **kwargs):
        """
        open application by package name.
        :param package_name: package name
        :param kwargs:
        :return:
        """
        self.device.session(package_name, **kwargs)

    def scroll_to_end(self):
        """
        if current screen exist scrollable UI, scroll it to end.
        """
        self.device(scrollable=True).scroll.toEnd()


def create_action(device):
    """
    return an action object for device.
    :param device: Android or IOS device
    :return: AndroidAction or IOSAction
    """
    return AndroidAction(device)
