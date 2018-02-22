import urllib2
import json
import datetime


mylist=[]
mylist1=[]
list2=[]
cur_date=datetime.datetime.now()
def compare_lists(l1,l2):
    s=0
    for i in l1:
        if i in l2:
            s+=1
    return s
s = raw_input("enter 10 numbers separated by a single space: ")
numbers = map(int, s.split())
print numbers
for i in range(31):
		cur_date= cur_date - datetime.timedelta(days=1)
		date_str= cur_date.strftime("%d-%m-%Y")
		url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
		req = urllib2.Request(url)
		response = urllib2.urlopen(req)
		data = response.read()
		data=json.loads(data)
		klhrwseis= data['draws']['draw']
		r=[]
		for k in klhrwseis:
			tmp=k["results"]
			r.append(compare_lists(numbers,tmp))
	
		if (r>4):
			mylist.append(max(r))
			mylist1.append(date_str)

		

zipped=zip(mylist,mylist1)
print zipped
x=max(mylist)
print  10*"-"
print "oi hmeromhnies me tis perissoteres epituxies einai: "
for i in range(len(mylist)):
  if mylist[i]== x:
	 print mylist1[i]
		

