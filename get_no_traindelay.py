#Script to scrap data
# Script to resolve the mins
#**********************************************Mains***********************************
# Script starts here
import xlrd
import math
import re
# Open workbook
import shelve
halt=shelve.open("C:\\Users\\Tarun Khajuria\\Desktop\\Indian Railways\\Data Late Trains\\15_5.dat")
hours={}
number={}
maxi={}
default=0
total_time=0
late_trains={}
book=xlrd.open_workbook('C:\\Users\\Tarun Khajuria\\Desktop\\Indian Railways\\ASSETS FAILURES FROM APRIL TO MAY 2015\\May 2015\\15.05.15.xlsx')
sheet=book.sheet_by_index(0)
print sheet.nrows
for row in range(4,sheet.nrows):
	rowe=sheet.row(row)
	fault=rowe[3].value	
	fault=fault.replace(" ","")
	no_trains=rowe[11].value
	if(fault!="" and type(no_trains)==float):
	# Check for cell type date
		if(late_trains.has_key(fault)):
			late_trains[fault]=late_trains[fault]+int(no_trains)
		else:
			late_trains[fault]=int(no_trains)
	else:
		default=default+1
halt['trainslate']=late_trains
halt.close()
print late_trains
print default
