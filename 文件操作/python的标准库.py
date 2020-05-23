# 引入sys模块
import sys
import pprint

sys.argv
# 获取执行代码时，命令行中所含的参数
# python(命令) python的标准库.py(参数)
print(sys.argv)  # 该属性是一个列表，列表中保存了当前命令的所有参数
# 第一个是模块名，第二个是函数
# pprint.pprint(sys.modules)  # 自动换行

# sys.path
# ['D:\\Uni\\SS20\\DuA\\Aufgabe1\\文件操作',
#  'D:\\Uni\\SS20\\DuA\\Aufgabe1',
#  'C:\\Users\\xian2\\AppData\\Local\\Programs\\Python\\Python38-32\\python38.zip',
#  'C:\\Users\\xian2\\AppData\\Local\\Programs\\Python\\Python38-32\\DLLs',
#  'C:\\Users\\xian2\\AppData\\Local\\Programs\\Python\\Python38-32\\lib',
#  'C:\\Users\\xian2\\AppData\\Local\\Programs\\Python\\Python38-32',
#  'C:\\Users\\xian2\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages']
# 打印模块的搜索路径
pprint.pprint(sys.path)

# sys.platform 表示python当前运行的平台
print(sys.platform)

# sys.exit('程序退出！')  # 程序退出

# os模块让我可以对操作系统进行访问
import os  # 引入模块

# os.environ
# 获取系统的环境变量
# pprint.pprint(os.environ['path'])
# print(os)

# os.system() 可以用来执行操作系统的名字
os.system('dir')
