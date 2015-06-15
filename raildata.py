#Script to scrap data
# Script to resolve the mins
def resolveMins(time):
	if(time.ctype==3):
		time=time.value;
		if(time<=1):
			time=time*1440
		else:
			time=0
		return time
	else:
		time=time.value
		hour=0;
		mins=0;
		#Cell type string
		if(type(time)==unicode):
			spl=time.split(':')
			if(len(spl)>1):
				hour=int(re.sub("[^0-9]", "",spl[0]))
				mins=int(re.sub("[^0-9]", "",spl[1]))
			else:
				spl=time.split(';')
				if(len(spl)>1):
					hour=int(re.sub("[^0-9]", "",spl[0]))
					mins=int(re.sub("[^0-9]", "",spl[1]))
				else:
					try:
						mins=int(re.sub("[^0-9]", "",time))
					except:
						return -1
			mins=hour*60+mins
			return mins
		elif(type(time)==float):
			mins=time
			return mins
#**********************************************Mains***********************************
# Script starts here
import xlrd
import math
import re
# Open workbook
import shelve
halt=shelve.open("C:\\Users\\Tarun Khajuria\\Desktop\\Indian Railways\\Data Late\\15_5.dat")
hours={}
number={}
maxi={}
default=0
total_time=0
late_trains=0
book=xlrd.open_workbook('C:\\Users\\Tarun Khajuria\\Desktop\\Indian Railways\\ASSETS FAILURES FROM APRIL TO MAY 2015\\May 2015\\15.05.15.xlsx')
sheet=book.sheet_by_index(0)
for row in range(4,sheet.nrows):
	rowe=sheet.row(row)
	fault=rowe[3].value	
	fault=fault.replace(" ","")
	no_trains=rowe[11].value
	time=resolveMins(rowe[12])
	if(time>=0 and fault!="" and type(no_trains)==float):
		total_time=total_time+(time*int(no_trains))
		late_trains=late_trains+int(no_trains)
	# Check for cell type date
		if(hours.has_key(fault)):
			hours[fault]=hours[fault]+(time*int(no_trains))
			number[fault]=number[fault]+1
			if(maxi[fault]<time):
				maxi[fault]=time
		else:
			hours[fault]=time*int(no_trains)
			number[fault]=1
			maxi[fault]=time
	else:
		default=default+1
halt['hours']=hours
halt['number']=number
halt['maximum']=maxi
halt['defauter']=default
halt['total']=total_time
halt['trains_late']=late_trains
halt.close()
print hours
print number
print maxi
print total_time
print late_trains
print default	

