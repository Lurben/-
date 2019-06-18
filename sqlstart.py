#功能：创建表
#作者：李柳斌
#2019-6-17

import pymysql

#打开数据库连接
db = pymysql.connect("localhost","root","","electronic_components_warehouse")

#创建游标cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS electronic_components")

#创建数据库表
sql = """CREATE TABLE electronic_components (  
         name  CHAR(20) NOT NULL,
         type  CHAR(20) NOT NULL,
         amounts INT DEFAULT 0,  
         attribute_identification CHAR(255),
         price  FLOAT NOT NULL,
         time TIMESTAMP NOT NULL,        
         monthly_consumption INT DEFAULT 0 )"""
cursor.execute(sql)

# 提交到数据库执行
db.commit()

# 关闭数据库连接
db.close()