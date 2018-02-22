import random
myList = random.sample(xrange(-30 , 30) , 30 )
result = []
myList.sort()
print "oi tuxaioi arithmoi einai: "
print myList
result = []
for i in range(0, len(myList)-2):
    for j in range(i + 1, len(myList)-1):
        for k in range(j + 1, len(myList)):
			if not sum([myList[i], myList[j], myList[k]]):  
				result.append([myList[i], myList[j], myList[k]])
							
unique_lst = []
[unique_lst.append(sublst) for sublst in result if not unique_lst.count(sublst)]
if not unique_lst :
	print "den vrethikan triades"
print 30*"-"
print "oi dunatoi sunduasmoi triadwn einai: "
print unique_lst