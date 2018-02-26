# -*- coding: utf-8 -*-
"""
==============================
   Date:           01_31_2018  11:43
   File Name:      /GitHub/company_forum
   Creat From:     PyCharm
   Python version:   
- - - - - - - - - - - - - - - 
   Description:
==============================
"""

import logging

__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)

def pp_dbg(*args):
    return logging.debug(*args)



