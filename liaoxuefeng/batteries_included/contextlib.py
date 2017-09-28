import contextlib
import os
import re
#在python中打开文件需要写try finally语句来关闭打开的通道
str1 = os.getcwd()



r = r'^(\d)+y$'
match = re.match(r,'33yddd')
print(match)

# print(groups.group(1))


# try:
    # f = open("/oriented2object/text.py",'r')
    # f.read()
# finally:
    # f.close()