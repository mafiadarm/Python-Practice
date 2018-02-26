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


def printdbg(*args):
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
                PRIMARY KEY (key_id)'''
        INT: set type like [CHAR(20), FLOAT, ...]
        NOT NULL: set it must have value, except return error.
        AUTO_INCREMENT: get serial number for auto
        PRIMARY KEY: set primary key, use "," split to set more
        """
        # if table exists, use execute() to delete.
        sentence = "DROP TABLE IF EXISTS %s" % table_name
        self.cur.execute(sentence)

        # use SQL sentence creat table
        sql = "CREATE TABLE {} ({})".format(table_name, fields)
        self.cur.execute(sql)

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

        try:
            # 执行sql语句
            self.cur.execute(sql)
            # 提交到数据库执行
            self.conn.commit()
        except Exception:
            # Rollback in case there is any error
            self.conn.rollback()
        finally:
            self.connClose()


def queryData():
    """
    Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。
    fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
    fetchall():接收全部的返回结果行.
    rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
    """

    # SQL 查询语句
    sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % 1000  # 查询EMPLOYEE表中salary（工资）字段大于1000的所有数据
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            # 打印结果
            print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % (fname, lname, age, sex, income))
    except Exception:
        print("Error: unable to fecth data")
    finally:
        connClose(cursor, db)


def upgradeData():
    """
    更新操作用于更新数据表的的数据，以下实例将 EMPLOYEE 表中的 SEX 字段为 'M' 的 AGE 字段递增 1：
    """
    cursor = db.cursor()

    # SQL 更新语句
    sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % 'M'
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except Exception:
        # 发生错误时回滚
        db.rollback()
    finally:
        connClose(cursor, db)


def deleteData():
    """
    删除操作用于删除数据表中的数据，以下实例演示了删除数据表 EMPLOYEE 中 AGE 大于 20 的所有数据：
    """
    cursor = db.cursor()

    # SQL 删除语句
    sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % 20
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交修改
        db.commit()
    except Exception:
        # 发生错误时回滚
        db.rollback()
    finally:
        connClose(cursor, db)


def performIntroduce():
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


def errorIntroduce():
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
