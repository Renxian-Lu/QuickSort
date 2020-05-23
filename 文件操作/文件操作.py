# 操作文件步骤
# 打开 对文件进行操作(读，写) 关闭文件
# open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
# file: 文件名(路径)
# r 可以使用原始字符
# ..返回一级目录
file_name = '../demon'
file_obj = open(file_name)
# open返回一个对象：当前打开的文件
# 在同一目录下，直接使用文件名
# 距离当前文件比较远，使用绝对路径
print(file_name)
print(file_obj)

# 读取文件中的内容，全部保存为字符串返回
# content = file_obj.read()
# print(content)

# 关闭文件
# file_obj.close()

with open(file_name) as file_obj:
    # 在with中可以直接使用file_obj来做文件操作
    content = file_obj.read()
    print(content)