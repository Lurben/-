#功能：主函数，实现功能
#作者：李柳斌
#2019-6-17

import pymysql
from goto import with_goto

#出库
@with_goto
def reduce():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "", "electronic_components_warehouse")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    name = input("请输入要出库的元件名：")
    old = "SELECT * FROM electronic_components WHERE name = '%s'" % name
    res = cursor.execute(old)
    old_result = cursor.fetchone()
    if res == 0:
        print("%s元件已没有库存或者尚未入库" % name)
    else:
        print("%s元件当前库存为%s" % (name, old_result[2]))

        number = int(input("请输入出库数目："))
        label .restart
        if number > old_result[2]:
            print("元件出库数目不能大于库存数！")
            number = int(input("请重新输入出库数目："))
            goto .restart
        else:
            sql1 = "UPDATE electronic_components SET amounts = amounts - %d WHERE name = '%s'" % (number, name)
            sql2 = "UPDATE electronic_components SET monthly_consumption = monthly_consumption + %d WHERE " \
                   "name = '%s'" % (number, name)
            try:
                # 执行SQL语句
                cursor.execute(sql1)
                cursor.execute(sql2)
                # 提交修改
                db.commit()
            except:
                # 发生错误时回滚
                db.rollback()
            print("出库成功！")
    cursor.close()

