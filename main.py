#功能：主函数，实现功能
#作者：李柳斌
#2019-6-17


import store, query, warn, reduce, statistics

def main():
	# 功能选择
	print("+---------------请选择操作：------------+\n")
	print("1.--------入库--------\n")
	print("2.--------出库--------\n")
	print("3.--------查询--------\n")
	print("4.--------统计--------\n")
	warn.warn()
	str = int(input("\n请输入："))

	#功能实现
	if str == 1:
		store.store()
	elif str == 2:
		reduce.reduce()
	elif str == 3:
		query.query()
	elif str ==4:
		print("------------统计功能---------\n")
		print("1.----------库元件总价值统计---------------\n")
		print("2.----------每月出库元件总价值统计---------\n")
		print("3.----------各类元件本月消耗量-------------\n")
		first_value = int(input("请选择统计类："))
		statistics.statistics(first_value)


if __name__ == '__main__':
    main()