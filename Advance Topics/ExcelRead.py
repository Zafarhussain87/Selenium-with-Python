import xlrd
import xlwt

"""workbook = xlrd.open_workbook("D:\\java\\PracticeTestCase\\data\\testdata.xlsx")
sh = workbook.sheet_by_index(0)
rows = sh.nrows
cols = sh.ncols

data=[]
for row in range(0,rows):
    for col in (0, cols-1):
        res = sh.cell(row,col).value
        data.append(res)
print(data)"""

import pandas as pd
xlfile = pd.ExcelFile("D:\\java\\PracticeTestCase\\data\\testdata.xlsx")

df = xlfile.parse(xlfile.sheet_names[0])

print(df)

