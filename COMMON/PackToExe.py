# -*- coding: utf-8 -*-
"""
==============================
   Date:           02_24_2018  13:50
   File Name:      /GitHub/install_py
   Creat From:     PyCharm
- - - - - - - - - - - - - - - 
   Description:
   在windows下，把py文件打包成win系统下的exe文件
==============================
"""
import logging
import os
import platform

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


def printdbg(*args):
    return logging.debug(*args)


class PackUp:
    def __init__(self, file_path, ico_path=None, option=""):
        self.file = file_path
        self.icon = ico_path
        self.option = option
        if platform.system() == "Windows":
            self.pack_exe()

    def ico_exists(self):
        """
        ensure file and icon
        :return:
        """
        if self.icon and not os.path.exists(self.icon):
            return False
        return True

    def pack_exe(self):
        """

        常用参数说明：
        –icon=图标路径
        -F 打包成一个exe文件
        -w 使用窗口，无控制台
        -c 使用控制台，无窗口
        -D 创建一个目录，里面包含exe以及其他一些依赖性文件

        For Example: [pyinstaller -F --icon=<ico_path>.ico <file_path>/<filename>.py]
        """
        if not self.ico_exists():
            return "check icon path"

        if self.icon and os.path.exists(self.file):
            command = "pyinstaller -F {} --icon={} {}".format(self.option, self.icon, self.file)
        elif not self.icon and os.path.exists(self.file):
            command = "pyinstaller -F {} {}".format(self.option, self.file)
        else: command = "echo check path"

        os.system(command)
        print("U can get <file>.exe in {}".format(os.getcwd()))

if __name__ == '__main__':
    PackUp("./zhilianzhaopin_threading.py")