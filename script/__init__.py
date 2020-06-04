#!/usr/bin/python
# -*- coding: UTF-8 -*-

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    port="3306",
    user="root",  # 数据库用户名
    passwd="alixian",  # 数据库密码
    database="T_User_Profile"
)


def read_scv():
    fo = open("/Users/LeeXian/压缩包/2.csv", "r")
    a = 0
    while True:
        line = fo.__next__()
        line = line.replace("\\N", "")
        result = ""
        columns = line.split(",")
        if len(columns) != 29:
            a = a + 1
            print("当前a的值：", a)
            print(line)
            print("========================")

            continue
        # for item in columns:
        #     if "" != result:
        #         result = result + ",\"" + item + "\""
        #     else:
        #         result = "\"" + item + "\""
        # print(result)
        # myCursor = mydb.cursor()
        # sql = "INSERT INTO T_userInfo_flush (c1, c2,c3, c4,c5, c6,c7, c8,c9, c10,c11, c12,c13, c14,c15, c16,c17, c18,c19, c20,c21, c22,c23, c24,c25, c26,c27, c28,c29) VALUES (" + result + ")"
        # myCursor.execute(sql)
        # mydb.commit()


try:
    read_scv()
except StopIteration:
    print("遍历完成")

print("读取完毕")
