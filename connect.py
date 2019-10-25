#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Auth : miaowei
# @Time : 2019/xx/xx
# description: 连接数据库

from pymysql import *


class Connect:

    def __init__(self, host, user, passwd, db, port=3306):
        self.conn = connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
        self.cursor = self.conn.cursor()

    def select(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        self.conn.commit()
        return result

    def insert(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

    def __del__(self):
        # 关闭游标
        self.cursor.close()
        # 关闭连接
        self.conn.close()
