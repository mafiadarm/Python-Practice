#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
   Date:           02_24_2018  21:50
   File Name:      /GitHub/MysqlUse
   Creat From:     PyCharm
- - - - - - - - - - - - - - - 
   Description:
   First, already install pymysql module
   add delete update search
   use sql sentence is emphasis
   [http://www.runoob.com/sql/sql-tutorial.html] search sql grammar
==============================
"""
import logging
import pymysql

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


def pp_dbg(*args):
    return logging.debug(*args)


class MysqlUse:
    def __init__(self, **kwargs):
        self.port = kwargs.get("port")
        self.host = kwargs.get("host")
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")
        self.database = kwargs.get("database")

        self.conn = self.connect()
        self.cur = self.conn.cursor()

    def connClose(self):
        """
        close connect
        Warning the order in sequence [cur > conn]
        """
        self.cur.close()
        self.conn.close()

    def connect(self):
        """
        already creat database DATABASE.
        already creat table EMPLOYEE in DATABASE.
        already creat username "username" and password "password" to connect DATABASE.
        * U can set by yourself or use "root" with its password.
        * Mysql authorization use command [Grant] Please!

        # use method [cursor()] to get cursor [for example: cur = database.cursor()]
        # use method [fetchone()] to get a data [for example: data = cursor.fetchone()]
        # use method [execute()] to execute sentence [for example: cursor.execute("SELECT ***")]
        """
        if not self.port: self.port = 3306
        if not self.username or not self.password:
            return pymysql.connect(host=self.host, db=self.database, port=self.port, charset='utf8')
        elif not self.database:
            return pymysql.connect(host=self.host, port=self.port, user=self.username, password=self.password, charset='utf8')
        else:
            return pymysql.connect(host=self.host, db=self.database, port=self.port, user=self.username, password=self.password, charset='utf8')

    def creatTable(self, table_name, fields):
        """
        already connect database
        already get the cursor
            this example for creat table EMPLOYEE
            EMPLOYEE filed [FIRST_NAME, LAST_NAME, AGE, SEX, INCOME]
        :param table_name: table name
        :param fields: for example: '''
                key_id        INT         NOT NULL      AUTO_INCREMENT
                FIRST_NAME    CHAR(20)    NOT NULL,
                LAST_NAME     CHAR(20),
                AGE           INT,
                SEX           CHAR(1),
                INCOME        FLOAT
                PRIMARY KEY (key_id)
                '''
        INT: set type like [CHAR(20), FLOAT, ...]
        NOT NULL: set it must have value, except return error.
        AUTO_INCREMENT: get serial number for auto
        PRIMARY KEY: set primary key, use "," split to set more
        """
        # if table exists, use execute() to delete.
        sentence = "DROP TABLE IF EXISTS %s" % table_name
        self.cur.execute(sentence)

        # use SQL sentence creat table
        sql = r"CREATE TABLE {}({});".format(table_name, fields)
        self.executeCommit(sql)

    def executeCommit(self, sql):
        """
        use sql sentence to all want
        :param sql: any sql sentence to be execution
        """
        try:
            # execute sentence
            self.cur.execute(sql)
            # Commit to database execution.
            self.conn.commit()
        except Exception:
            # Rollback in case there is any error
            self.conn.rollback()
        finally:
            pso.connClose()

    def insertRecord(self, fields, values):
        """
        already connect database
        already get the cursor
        or use: '''
            INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
            VALUES ('%s', '%s', '%d', '%c', '%d' )" % ('Mac', 'Mohan', 20, 'M', 2000)
            '''
        :param fields: for example: "FIRST_NAME, LAST_NAME, AGE, SEX, INCOME"
        :param values: correspondence fields [string or int or float]
        """
        # SQL insert
        sql = "INSERT INTO EMPLOYEE({}) VALUES ({})".format(fields, values)
        self.executeCommit(sql)

    def deleteData(self, table_name, conditions):
        """
        already connect database
        already get the cursor
        for example: delete table[EMPLOYEE]'s data when field[AGE] > 20
        "DELETE FROM {EMPLOYEE} WHERE {AGE > 20}"
        """
        # SQL delete
        sql = "DELETE FROM {} WHERE {}".format(table_name, conditions)
        self.executeCommit(sql)

    def upgradeData(self, table_name, content, condition):
        """
        already connect database
        already get the cursor
        for example: in table[EMPLOYEE] update field[AGE] growing 1 when field[SEX] is "M"
        "UPDATE {EMPLOYEE} SET {AGE = AGE + 1} WHERE {SEX = 'M'}"
        """
        # SQL upgrade
        sql = "UPDATE {} SET {} WHERE {}".format(table_name, content, condition)
        self.executeCommit(sql)

    def queryData(self, table_name, field_conditions=None):
        """
        already connect database
        already get the cursor
        use fetchone() get just one data, like next()
        use fetchall() get more data.
        row[count]: is read attribute，return execute() get row.
        grammar: SELECT * FROM {table_name} WHERE {field_conditions}
        for example: search all data in table[EMPLOYEE] field[salary] > 1000
        "SELECT * FROM {EMPLOYEE} {WHERE salary > 1000}"
        :param table_name: search table
        :param field_conditions: example: field_one > num and/or field_two = num
        """
        # SQL query
        sql = "SELECT * FROM {} {}".format(table_name, field_conditions)  # 查询EMPLOYEE表中salary（工资）字段大于1000的所有数据
        try:
            # execute sql sentence
            self.cur.execute(sql)
            # get all record in list
            results = self.cur.fetchall()
            for row in results:
                print(row)
        except Exception:
            print("Error: unable to fetch data")
        finally:
            pso.connClose()

    def performIntroduce(self):
        """
        事务机制可以确保数据一致性。

        事务应该具有4个属性：原子性、一致性、隔离性、持久性。这四个属性通常称为ACID特性。

        原子性（atomicity）。一个事务是一个不可分割的工作单位，事务中包括的诸操作要么都做，要么都不做。
        一致性（consistency）。事务必须是使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切相关的。
        隔离性（isolation）。一个事务的执行不能被其他事务干扰。即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰。
        持久性（durability）。持续性也称永久性（permanence），指一个事务一旦提交，它对数据库中数据的改变就应该是永久性的。接下来的其他操作或故障不应该对其有任何影响。
        Python DB API 2.0 的事务提供了两个方法 commit 或 rollback。
        """
        pass

    def errorIntroduce(self):
        """
        Warning	当有严重警告时触发，例如插入数据是被截断等等。必须是 StandardError 的子类。
        Error	警告以外所有其他错误类。必须是 StandardError 的子类。
        InterfaceError	当有数据库接口模块本身的错误（而不是数据库的错误）发生时触发。 必须是Error的子类。
        DatabaseError	和数据库有关的错误发生时触发。 必须是Error的子类。
        DataError	当有数据处理时的错误发生时触发，例如：除零错误，数据超范围等等。 必须是DatabaseError的子类。
        OperationalError	指非用户控制的，而是操作数据库时发生的错误。例如：连接意外断开、 数据库名未找到、事务处理失败、内存分配错误等等操作数据库是发生的错误。 必须是DatabaseError的子类。
        IntegrityError	完整性相关的错误，例如外键检查失败等。必须是DatabaseError子类。
        InternalError	数据库的内部错误，例如游标（cursor）失效了、事务同步失败等等。 必须是DatabaseError子类。
        ProgrammingError	程序错误，例如数据表（table）没找到或已存在、SQL语句语法错误、 参数数量错误等等。必须是DatabaseError的子类。
        NotSupportedError	不支持错误，指使用了数据库不支持的函数或API等。例如在连接对象上 使用.rollback()函数，然而数据库并不支持事务或者事务已关闭。 必须是DatabaseError的子类。
        """
        pass

if __name__ == '__main__':
    cc = {
        "host": "localhost",
        "username": "root",
        "password": "123456",
        "database": "abc"
    }
    table_field = '''
    key_id INT NOT NULL AUTO_INCREMENT,
    FIRST_NAME CHAR(20) NOT NULL,
    LAST_NAME CHAR(20),
    AGE INT,
    SEX CHAR(1),
    INCOME FLOAT,
    primary key (key_id)
    '''
    pso = MysqlUse(**cc)
    # sqls = "create table test(key_id INT NOT NULL AUTO_INCREMENT, FIRST_NAME CHAR(20) NOT NULL, LAST_NAME CHAR(20),AGE INT,SEX CHAR(1),INCOME FLOAT)"
    # sqls = "INSERT INTO tt(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('%s', '%s', '%d', '%c', '%d' )" % ('Mac', 'Mohan', 20, 'M', 1234)
    # pso.executeCommit(sqls)
    # pso.creatTable("tt", table_field)
    # pso.queryData("tt")
    # pso.upgradeData("tt","INCOME = 500", "sex = 'M'")
