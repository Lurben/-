#功能：主函数，实现功能
#作者：李柳斌
#2019-6-17

#功能：查询
#作者：李柳斌
#2019-6-17

import pymysql
import datetime,time
def query():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "", "electronic_components_warehouse", 3306)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "", "electronic_components_warehouse")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    query_type = input("请输入要查询的类型：")
    # SQL 查询语句
    sql = "SELECT * FROM electronic_components WHERE type = '%s'" % query_type
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        n = 0  #计数
        for row in results:
            n = n+1
            query_name = row[0]
            query_number = row[2]
            query_identification = row[3]
            query_price = row[4]
            query_addtime = row[5]
            print("%d.元件名称：%s  库存数：%d个  " % (n, query_name, query_number), end="")
            print("单价：%d元  入库时间：%s" % (query_price, query_addtime))
            print("属性标识：%s\n" % (query_identification))
    except:
        print("发生错误！无法连接到数据库！！！")
    cursor.close()