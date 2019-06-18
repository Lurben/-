#功能：主函数，实现功能
#作者：李柳斌
#2019-6-17
#入库
import pymysql
import datetime


def store():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "", "electronic_components_warehouse", 3306)

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    name = input("请输入元件名：")
    type = input("请输入元件类型：")
    amounts = input("请填写入库新增元件数目：")
    attribute_identification = input("请填写元件属性标识：")
    price = input("请输入元件单价：")
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")
    old = "SELECT * FROM electronic_components WHERE name = '%s'" % (name)
    res = cursor.execute(old)
    if res == 0:
        # SQL 插入语句
        sql = """INSERT INTO electronic_components(name, type, amounts,
                 attribute_identification, price, time, monthly_consumption)
                 VALUES (%s, %s, %s, %s, %s, %s, 0)"""
        try:
            # 执行sql语句
            cursor.execute(sql, (name, type, amounts, attribute_identification, price, now))
            # 提交到数据库执行
            db.commit()
            print("入库成功！")
        except:
            # 如果发生错误则回滚
            print('插入失败')
            db.rollback()

    else:
        sql = "UPDATE electronic_components SET amounts = new_amounts + amounts WHERE name = '%s'" % (name)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()
    # 关闭数据库连接
    db.close()

