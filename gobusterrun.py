import webbrowser
import requests
import time
import os
whoami=os.getcwd()
url=open(str(whoami)+"/url.txt","r").read()
file=open(str(whoami)+"/mrx.txt","r").read()
url=url.strip("\n")
w=""
arr=[]
x=0
idk=True
for i in file:
	if i == "/":
		w=""
		idk=True
		x=x+1

	if idk == True:
		w=w+i

	if i == " ":
		idk=False

	f2=w.find("[")
	f3=w.find("]")
	if idk == False and  w !="" and f3 == -1:
		arr.append(w)
		w=""
		x=0
for x in arr:
	try:
		x=x.strip(" ")
		x=str(x)+"/"
		mrx=str(url)+str(x)
		a=requests.head(mrx)
		print(mrx," ",a)
		if str(a) != "<Response [400]>" and str(a) != "<Response [401]>" and str(a) != "<Response [404]>" and str(a)!= "<Response [503]>" and str(a) != "<Response [403]>":
			webbrowser.open(mrx)
			time.sleep(1)
	except:
		continue
