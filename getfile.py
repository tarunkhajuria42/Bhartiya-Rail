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
	dicti=obj['index']
	sheet.write(1,date[fil],fil)
	for key in dicti.keys():
		if key in cate.keys():
			sheet.write(cate[key],date[fil],dicti[key])
		else:
			cate[key]=len(cate.keys())+2
			sheet.write(cate[key],0,key)	
			sheet.write(cate[key],date[fil],dicti[key])
	obj.close()
book.save("C:\\Users\\Tarun Khajuria\\Desktop\\Indian Railways\\Data New\\index.xls")