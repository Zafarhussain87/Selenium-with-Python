import xlwt
import xlsxwriter

import xlrd

workbook = xlsxwriter.Workbook("D:\\java\\PracticeTestCase\\data\\pyt.xlsx")
sheet = workbook.add_worksheet()

sheet.write(0,0,556)
sheet.write(0,1, "last")
sheet.write(1,0,"alpha")
sheet.write(1,1,"beta")
workbook.close()