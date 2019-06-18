#功能：主函数，实现功能
#作者：李柳斌
#2019-6-17

#功能：创建表
#作者：李柳斌
#2019-6-17

import pymysql

#报警
def warn():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "", "electronic_components_warehouse", 3306)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM electronic_components WHERE amounts < %d" % (100)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            warn_name = row[0]
            warn_number = row[2]
            print("！！！警报：%s库存不足，仅剩%d个" % (warn_name, warn_number))
    except:
        print("发生错误！无法连接到数据库！！！")
    cursor.close()


