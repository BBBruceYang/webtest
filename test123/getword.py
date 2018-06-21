#從txt檔中擷取需要的資訊出來
#這次做的是從irgo.txt中抓出systeminfo資訊
import linecache
import re

with open('irgo.txt') as f:
	lines = f.readlines()
	infostart = 'systeminfo';
	infoend = '登入伺服器'
	count = 0
	#i = 0
	#j = 0
		#找出起始的行數
	for line in lines:
		if infostart in line:
			print (line)
			print (count)
			i = count
		if infoend in line:
			print (line)
			print (count)
			j = count
		else: 
			count += 1
	"""infoend = '登入伺服器';
		#找出終止的行數
	j = 0
		if infoend in line:
			print (line)
			print (j)
			break
		else:
			j += 1
	"""
	print ("finish")
	print ("起始的行數=", i, "結束的行數", j)
	print (lines[i:j])
	a = (lines[i:j])
	a = [item.replace("\n", "<br/>") for item in a]
	print (a)
	a = "".join(a)
	print (a)