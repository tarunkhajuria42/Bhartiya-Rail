# Python Script to pickle data to day wise failure
#Time: The time to be converted
#hours: True/False hours or specific time 
# 		True: Hours, False: Time
def resolveMins(time,hours):
	if(time.ctype==3):
		time=time.value;
		time=time*3600;
	else:
		time=time.value
		#Cell type float
		if(type(time)==float):
			l=math.modf(time)
			if(l[1]<24):
				time=l[0]+(l[1]*60)
			else:
				time=l[1]
		else:
			if(len(time)>0):
				splt=splittime(time)
				if(splt>=0):
					time=splt
				else:
					default=default+1
			else:
				default=default+1
	time=time.replace('\"',"")
	spl=time.split(':')
	if(len(spl)>1):
		hour=int(spl[0])
		mins=int(spl[1])
	else:
		spl=time.split('.')
		if(len(spl)>1):
			print(spl)
			hour=int(re.sub("[^0-9]", "",spl[0]))
			mins=int(re.sub("[^0-9]", "",spl[1]))
		else:
			spl=time.split('.')
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

# Get the duration between two times
def getDuration(starttime,endtime):
	endtime=resolveMins(endtime)
	starttime=resolveMins(starttime)
	if(endtime==-1 or starttime==-1):
		return -1
	duration=starttime-endtime
	if(duration<0):
		duration=24-duration
	return duration
# Script starts here
import xlrd
import math
import re
# Open workbook
import shelve
halt_hours=shelve.open("C:\\Users\\Tarun Khajuria\\Desktop\\Indian Railways\\Scripts\\hours.dat")
halt_number=shelve.open("C:\\Users\\Tarun Khajuria\\Desktop\\Indian Railways\\Scripts\\number.dat")
hours={}
number={}
maxi={}
rows=[]
cols=[]
book=xlrd.open_workbook('C:\\Users\\Tarun Khajuria\\Desktop\\Indian Railways\\ASSETS FAILURES FROM APRIL TO MAY 2015\\April 2015\\04.04.15.xlsx')
sheet=book.sheet_by_index(0)
default=0
for row in range(4,211):
	rowe=sheet.row(row)
	fault=rowe[3].value
	fault=fault.replace(" ","")
	if(fault==""):
		print row
	time=rowe[7]
	# Check for cell type date
		if(hours.has_key(fault)):
			hours[fault]=hours[fault]+time
			number[fault]=number[fault]+1
		else:
			hours[fault]=time
			number[fault]=1
print hours
print number
print default	



		