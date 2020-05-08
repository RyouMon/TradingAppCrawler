#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Actor:
    """
    Base Actor.
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


class AndroidActor(Actor):
    """
    An actor for Android, interactive with Android device
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


def create_actor(device):
    """
    return an actor object for device.
    :param device: Android or IOS device
    :return: AndroidActor or IOSActor
    """
    return AndroidActor(device)
