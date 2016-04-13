#coding=utf-8
import MySQLdb
conn = MySQLdb.connect(host="localhost",user="root",passwd="root",db="test",port=3306,charset="utf8")
cur =conn.cursor() #游标对象