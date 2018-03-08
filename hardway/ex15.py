from sys import argv # 调用sys的argv

script, filename = argv # 用argv 获取文件名，script，filename，只是变量名，随便起的不影响。但是如何判断找到的是我们预定的文件呢？用户输入

txt = open(filename) # 打开输入的第二个参数对应文件

print("here's your file %r:" % filename) # 读取第二个参数对应文件的名字
print(txt.read()) #显示第二个参数对应文件的内容

print("Type the filename again:") # 进行第二种打开文件的方法
file_again = input(">") # 输入要打开文件的名字

txt_again = open(file_again) # 打开

print(txt_again.read())# 显示