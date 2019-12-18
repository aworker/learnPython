import xlrd
import re

str_candicate = '李明远'

excel_data = xlrd.open_workbook('wuyunlong.xlsx')

sheet_objs = excel_data.sheets()


def transform(st):
    findall = re.findall(r'\d+', st)
    if len(findall) == 0:
        return 0
    day_num = int(findall[0]) * 1 * 24 * 60 * 60
    hour_num = int(findall[1]) * 1 * 60 * 60
    minute_num = int(findall[2]) * 1 * 60
    second_num = int(findall[3]) * 1
    total_num = day_num + hour_num + minute_num + second_num
    return total_num


num = 0
hour_of_24 = 24 * 60 * 60

for sheet in sheet_objs:
    sheet_ncols = sheet.ncols
    sheet_nrows = sheet.nrows
    row_data_0 = sheet.row_values(0)
    for row_num in range(0, sheet_nrows):
        row_data = sheet.row_values(row_num)
        flag = False
        record_time = 0
        for col_num in range(0, sheet_ncols):
            # if flag :
            #     continue
            data_row_col = row_data[col_num]
            str_value = str(data_row_col)
            if str(row_data_0[col_num]) == '当前经办人' or '解决人' in str(row_data_0[col_num]):
                # print(str_value)
                continue
            if str_candicate == str_value:
                time_str = row_data[col_num + 5]
                # print(str(row_num)+':' +str(row_data_0[col_num]))
                # print(time_str)
                flag = True
                record_time = record_time + transform(time_str)
        if record_time > hour_of_24:
            print(row_data[0] +':' + str(record_time))


