# -*- coding: utf-8 -*-
"""
==============================
   Date:           01_25_2018  13:42
   File Name:      /GitHub/library_manage
   Creat From:     PyCharm
   Python version:   
- - - - - - - - - - - - - - - 
   Description:
==============================
"""

__author__ = 'Loffew'

import logging
import time

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)

class Book:
    def __init__(self):
        self.borrowList = {}  # 借出登记表
        self.bookList = {}  # 书架
        self.orderList = {}  # 预约登记表

    def addBook(self, bookname, bookauthor):
        time.sleep(0.001)
        self.bookList[time.time()] = (bookname, bookauthor)  # 新进的书放到书架

    def borrowBook(self, bookname, bookauthor,  patron):
        if (bookname, bookauthor) in self.bookList.values():  # 如果书在书架，代表可以借
            self.borrowList[(patron, time.time())] = (bookname, bookauthor)  # 记录到借出登记表
            move = [key for key in self.bookList if self.bookList.get(key) == (bookname, bookauthor)][0]
            self.bookList.pop(move)  # 从书架取下
            if (bookname, bookauthor,  patron) in self.orderList:  # 如果是在预约登记表中
                self.orderList.pop((bookname, bookauthor,  patron))  # 删除预约登记表中的记录

    def getBack(self, bookname, bookauthor, patron):
        move = [key for key in self.borrowList
                if key[0] == patron and self.borrowList.get(key) == (bookname, bookauthor)][0]
        self.borrowList.pop(move, "%s does not borrow this book" % patron)  # 从借出登记表中删除
        self.addBook(bookname, bookauthor)  # 书放回书架

    def orderBook(self, bookname, bookauthor, patron, borrowtime):
        timeArray = time.strptime(borrowtime, "%Y-%m-%d")
        timeArray = int(time.mktime(timeArray))
        if (bookname, bookauthor) in self.orderList.values():  # 如果预约已经有了
            if timeArray < [key[1] for key in self.orderList
                            if self.orderList.get(key) == (bookname, bookauthor) and key[0] == patron][0]:  # 而且时间靠前
                print("This book borrowed.")  # 不允许插队
            else: self.orderList[(patron, timeArray)] = (bookname, bookauthor)  # 如果时间靠后，则登记
        else: self.orderList[(patron, timeArray)] = (bookname, bookauthor)  # 如果没预约，直接登记


class Patron(Book):
    def __init__(self):
        super(Book, self).__init__()
        self.borrowlist = []  # 借到的书

    def borrowPatron(self, bookname, bookauthor, patron):
        if len(self.borrowlist) >= 3:  # 如果大于三本
            print("There will more than three book.")  # 不允许再借
        else:
            self.borrowlist.append((bookname, bookauthor, patron))  # 除此之外可以借
            return True

    def patronBack(self, bookname, bookauthor, patron):
        if (bookname, bookauthor, patron) in self.borrowlist:
            self.borrowlist.remove((bookname, bookauthor, patron))
            return True
        else: print("you never borrow this book")


class Library(Patron):
    def __init__(self):
        super(Library, self).__init__()
        super(Patron, self).__init__()

    def borrow(self, bookname, bookauthor, patron):
        if self.borrowPatron(bookname, bookauthor, patron):
            self.borrowBook(bookname, bookauthor, patron)

    def getback(self, bookname, bookauthor, patron):
        if self.patronBack(bookname, bookauthor, patron):
            self.getBack(bookname, bookauthor, patron)

    def orderbook(self, bookname, bookauthor, patron, borrowtime):
        self.orderBook(bookname, bookauthor, patron, borrowtime)


def main():
    """test"""
    ss = Library()
    books = ["book" + str(i) for i in range(3)]
    wons = ["won" + str(i) for i in range(3)]
    book_list = zip(books, wons)
    [ss.addBook(i, j) for i, j in book_list]

    print(ss.bookList)
    ss.borrow('book0', 'won0', "ren1")
    print(ss.borrowList)
    print(ss.borrowlist)
    print(ss.bookList)
    ss.getback('book0', 'won0', "ren1")
    print(ss.borrowList)
    print(ss.borrowlist)
    print(ss.bookList)

if __name__ == '__main__':
    main()