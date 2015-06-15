# Extracting shelve data to output index
import xlwt
import shelve
from os import listdir
files=listdir("C:\\Users\\Tarun Khajuria\\Desktop\\Indian Railways\\Data Late")
book=xlwt.Workbook(encoding="utf-8")
sheet=book.add_sheet("Dat")
date=shelve.open('C:\\Users\\Tarun Khajuria\\Desktop\\Indian Railways\\Dates')
date=date['new']
cate={}
for fil in files:
	obj=shelve.open("C:\\Users\\Tarun Khajuria\\Desktop\\Indian Railways\\Data Late\\"+fil)
	dicti=obj['trains_late']
	sheet.write(1,date[fil],fil)
	sheet.write(2,date[fil],dicti)
	obj.close()
book.save("C:\\Users\\Tarun Khajuria\\Desktop\\Indian Railways\\Data Late\\late.xls")