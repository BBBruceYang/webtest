#從txt檔中擷取需要的資訊出來
#這次做的是從irgo.txt中抓出systeminfo資訊
import linecache

with open('irgo.txt') as f:
	line = f.readline()
	infostart = 'systeminfo';
		#找出起始的行數
	i = 1
	for line in f:
		if not line.find(infostart) == -1:
			i+=1			
	infoend = '登入伺服器';
		#找出終止的行數
	print (i)
	j = i
	for line in f:
		if not line.find(infoend) == -1:
			j+=1
	print (i, j, "i跟j的行數")
	inforesult=linecache.getlines(f)[i:j]
	print (inforesult)