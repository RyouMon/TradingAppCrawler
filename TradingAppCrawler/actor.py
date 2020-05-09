#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod, ABC


class Actor(metaclass=ABCMeta):
    """
    An abstract class for actor.
    Perform basic operations on the device.
    """
    def __init__(self, device):
        self.device = device

    @abstractmethod
    def back(self):
        pass

    @abstractmethod
    def click_by_resource_id(self, resource_id):
        pass

    @abstractmethod
    def scroll_to_end(self):
        pass

    @abstractmethod
    def scroll_to_top(self):
        pass

    @abstractmethod
    def open_app(self, package_name):
        pass


class AndroidActor(Actor, ABC):
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

    def scroll_to_top(self):
        """
        if current screen exist scrollable UI, scroll it to top.
        """
        self.device(scrollable=True).scroll.toBeginning()


def create_actor(device):
    """
    return an actor object for device.
    :param device: Android or IOS device
    :return: AndroidActor or IOSActor
    """
    return AndroidActor(device)


if __name__ == '__main__':
    a = AndroidActor(None)