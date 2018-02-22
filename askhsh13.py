while True:
	n=int(raw_input("pliktrologeiste to plithos twn psifiwn: "))
	s=int(raw_input("pliktrologeiste to athroisma twn psifiwn: "))
	if n*9>=s:
		break
mik=10**(n-1)
meg=10**n-1
metr=0
listpsif=[]
for i in range(mik,meg+1):
	listpsif=[int(j)for j in str(i)]
	testpsif=1
	athr=0
	for k in range(n-1):
		if listpsif[k]<=listpsif[k+1]:
			testpsif+=1
		if testpsif==n:
			for k in range(n):
				athr+=listpsif[k]
	if athr==s:
		print i
