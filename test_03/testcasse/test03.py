import os
import time
import math
# os.mkdir("testdir")
# print(os.listdir("./"))
# print(os.getcwd())
# os.removedirs("testdir")
# print(os.path.dirname(__file__))
# print(os.path.exists("testdir"))
# if not os.path.exists("test03"):
#     os.makedirs("test03")

# os.removedirs("test03")
# print(time.asctime())
# print(time.localtime())
# print(time.time())
# tow_days_ago=time.time()+2*24*60*60
# time_t=time.localtime(tow_days_ago)
# print(time_t)
# print(time.strftime("%Y-%m-%d %H:%M:%S",time_t))
# var = 1

# print(math.sqrt(4))
# print(math.floor(3.2))
# print(math.ceil(4.3))
# from openpyxl import Workbook
# from openpyxl.utils import get_column_letter
# wb = Workbook()
# dest_filename = 'empty_book.xlsx'
# ws1 = wb.active
# ws1.title = "range names"
# for row in range(1, 40):
#      ws1.append(range(600))
#
# ws2 = wb.create_sheet(title="Pi")
# ws2['F5'] = 3.14
# ws3 = wb.create_sheet(title="Data")
# for row in range(10, 20):
#     for col in range(27, 54):
#        _ = ws3.cell(column=col, row=row, value="{0}".format(get_column_letter(col)))
# print(ws3['AA10'].value)
# wb.save(filename = dest_filename)

import yaml

print(yaml.load(open("demon.yaml"),Loader=yaml.FullLoader))

l=["a",{"b":{'a': 1, 'b': 2}},{"c":12}]
with open("demon.yaml","w") as f:
    yaml.safe_dump(data=l,stream=f)







