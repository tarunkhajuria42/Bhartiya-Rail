# Extracting shelve data to output index
import shelve
from os import listdir
files=listdir("C:\\Users\\Tarun Khajuria\\Desktop\\Indian Railways\\Data Late")
for fil in files:
	print fil
	obj=shelve.open("C:\\Users\\Tarun Khajuria\\Desktop\\Indian Railways\\Data Late\\"+fil)
	new={}
	dicti=obj['trains_late']
	for key in dicti.keys():
		new[key]=-100*dicti[key]/obj['total']
	obj['index']=new
	obj.close()
