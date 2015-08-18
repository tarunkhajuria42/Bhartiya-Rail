# Extracting shelve data to output index
import xlwt
import shelve
from os import listdir
files=listdir("C:\\Users\\GLADOS\\Desktop\\File")
book=xlwt.Workbook(encoding="utf-8")
sheet=book.add_sheet("Dat")
cate={}
for fil in files:
	obj=shelve.open("C:\\Users\\GLADOS\\Desktop\\File\\"+fil)
	dicti=obj['hours']
	sheet.write(1,obj['number'],fil)
	for key in dicti.keys():
		if key in cate.keys():
			sheet.write(cate[key],obj['number'],dicti[key])
		else:
			cate[key]=len(cate.keys())+2
			sheet.write(cate[key],0,key)	
			sheet.write(cate[key],obj['number'],dicti[key])
	obj.close()
book.save("C:\\Users\\GLADOS\\Desktop\\File\\timeLate.xls")