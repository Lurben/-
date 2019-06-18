#功能：创建表
#作者：李柳斌
#2019-6-17

import pymysql

def statistics(value):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "", "electronic_components_warehouse", 3306)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    if value == 1:
        total_statistics = 0
        sql_first = "SELECT * FROM electronic_components"
        try:
            # 执行SQL语句
            cursor.execute(sql_first)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                query_amounts = row[2]
                query_price = row[4]
                price = query_price*query_amounts
                total_statistics =total_statistics + price
            print("库内元件总价值为：%0.3f元" % (total_statistics))
        except:
            print("发生错误！无法连接到数据库！！！")
    elif value == 2 or value == 3:
        total_statistics = 0
        total_reduce = 0
        statistics_type = input("请输入要统计的元件类型：")
        # SQL 查询语句
        sql_first = "SELECT * FROM electronic_components WHERE type = '%s'" % statistics_type
        try:
            # 执行SQL语句
            cursor.execute(sql_first)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                query_price = row[4]
                query_reduce = row[6]
                price = query_price*query_reduce
                total_statistics = total_statistics + price
                total_reduce = total_reduce + query_reduce
        except:
            print("发生错误！无法连接到数据库！！！")
        if value == 2:
            print("%s类元件本月出库总价值为：%0.3f元" % (statistics_type, total_statistics))
        else:
            print("%s类元件本月消耗量为：%d个" % (statistics_type, total_reduce))
    else:
        print("非法输入！")
    cursor.close()
