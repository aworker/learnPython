import re



def transform(st):
    findall = re.findall(r'\d+', st)
    day_num = int(findall[0]) * 1 *24 * 60 * 60
    hour_num = int(findall[1]) * 1 * 60 * 60
    minute_num = int(findall[2]) * 1 * 60
    second_num = int(findall[3]) * 1
    print(day_num+hour_num+minute_num+second_num)

transform('0天1小时7分钟10秒')
