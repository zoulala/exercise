#coding=utf8



import json
#---------------------------------------------------------------
data = {1:['abc',3,4,10],'中国':9,'f':{'b':3,'k':[4,9,0]}}
print (data[1])
jdata = json.dumps(data)
print(jdata) # 1 变为了 ‘1’
print(type(jdata))

djdata = json.loads(jdata)
print(djdata)
print(type(djdata))
print (djdata[str(1)])
#--------------------------------------------------------------
f = open('jsonfile.dat','w')
json.dump(data,f)
f.close()
fp = open('jsonfile.dat','r')
dd = json.load(fp)
print(dd)
print(type(dd))
fp.close()

