import re


# \d 表示匹配一个数字 因为在python里面/是一个转义字符，所以要用//表示
s = '00\\d'
match = re.match(s, '004')
print(match)


# \w 表示匹配一个字母或者一个数字啊
s = r'\w\w\w'
match = re.match(s, 'a1b2c3d')
print(match)


# . 表示可以匹配任意一个字符

s=r'.'
match = re.match(s, '3d.de')
print(match)


#匹配和数量相关的字符个数 * 表示任意个数个字符 + 表示至少一个字符 ?表示0个或者1个字符 {n}表示n个字符 {n,m}表示n到m个字符范围内的都可以。

#写一个匹配带区号的电话号码匹配的正则表达式
s = r'\d{3}\s+\d{3,8}'   # \s 表示空格，可以是 space键的也可以是tab键的 所以 \s+表示至少有一个空格
match = re.match(s, '013  76551623')
print(match)

s = r'\d{3}\-\d{3,8}'  # - 是特殊的字符串，需要用到转译字符\
match = re.match(s, '110-12345678')
print(match)




#正如用{}可以很好的表示匹配字符数量，[]用来表示匹配的字符范围
#[0-9a-z] 表示匹配一个数字或者一个小写的英文字母
s = r'[0-9a-z]+'
match = re.match(s, 'abAa')
print(match)

s = r'[0-9][a-z]{0,4}' #表示匹配数字开头，然后由0到4个小写字母组成的字符串
match = re.match(s, '3adcdww')
print(match)

# A|B 表示可以匹配 A或者B
s = r'[P|p]ython'  #可以匹配Python 或者python这两种字符
match = re.match(s, 'Python')
print(match)

# ^表示行的开头必须是某种字符 $表示行的结尾必须是某种字符


# python 中用()表示要提取的分组
s = r'^(\d{3})-(\d{0,8})$'  #这里如果有分组，就不需要给- 加上转义字符\了。 加上后，反而错了。不知道为什么啊。
groups = re.match(s, '003-1233434')
print(groups.group(0))  # O 永远表示原来的字符串
print(groups.group(1))  # 1 表示第一个分组
print(groups.group(2))  # 2 表示第二个分组
print(type(groups.group(2))) #返回的是str类型的变量


s = r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])$' #匹配时间的小时位（24小时制）如 13 15 09 9 23 等都可以
match = re.match(s, '10')
match = re.match(s, '23')
match = re.match(s, '03')
print(match)


s = r'^([0-5][0-9]|[0-9])$' #匹配时间的 分钟位 如 00 03 09 10 19 20 29 30 39 50 59 等 秒位和分钟位是一样的
match = re.match(s,'59')
print(match)

s = r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:([0-5][0-9]|[0-9])\:([0-9]|[0-5][0-9])$' #匹配一个标准时间
match = re.match(s,'13:01:00')
print(match)



#正则表达式默认是使用贪婪匹配的，即尽可能多的匹配
s = r'^(\d+)(0*)$'
group = re.match(s, '100000')
print(group.group(2)) #因为是贪婪匹配 所以group.group(1)匹配了整个字符串 所以group.group(2)只能匹配空字符串了啊


print(re.match(r'^py$','py'))

























