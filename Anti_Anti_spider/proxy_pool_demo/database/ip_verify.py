#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           07_25_2018  10:50
    File Name:      /proxy_pool_demo/ip_verify
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
==============================
"""

from ipaddress import *


def ip_auth(address):
    try:
        return IPv4Address(address)
    except (AddressValueError, NetmaskValueError):
        try:
            return IPv6Address(address)
        except (AddressValueError, NetmaskValueError):
            return False


if __name__ == '__main__':
    print(ip_address("127.0.0.1"))
