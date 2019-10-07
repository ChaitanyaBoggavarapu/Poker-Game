class pokernew:
	def __init__(self, suitelist,valuelist):
		valuelist.sort()
		self.suitelist = suitelist
		#print(self.suitelist)
		self.valuelist = valuelist 
		self.what,self.value = self.poker(suitelist,valuelist)

	
	#def poker(self,suitelist,valuelist):
	def poker(self,suitelist,valuelist):
		if (suitelist[0]==suitelist[1]==suitelist[2]==suitelist[3]==suitelist[4]):
			x = "samesuit"
			valuelist = valuelist
			return self.checkRoyalorstraightflush(suitelist,valuelist)
		else:
			return self.checkOtherCases(suitelist,valuelist)
	def checkRoyalorstraightflush(self,suitelist,valuelist):	
		i,v = self.countAndVerify(suitelist,valuelist)	
		
		#if( valuelist[i]+1 == valuelist[i+1]):
		if (i==3 and valuelist[i+1]==14):
			return 'Royalflush',(max(valuelist))
		elif(i==3):
			return 'Straightflush',(max(valuelist))
		else:
			return 'flush',(max(valuelist))		
	def checkOtherCases(self,suitelist,valuelist):
		c,v = self.countAndVerify(suitelist,valuelist)
		if(c==3):
			return("Straight",v)	
		if(max(c)==3 and min(c)==2):
			return("FullHouse",v)
		if(max(c)==4):	
			return("Fourofakind",v)
		if(max(c)==3):
			return("Threeofakind",v)		
		if(c.count(2)==3 or c.count(2)==4):
			return("Twopair",v)
		if(max(c)==2):
			return("Onepair",v)
		if(max(c)==1):
			return("Nothing",v)
		
	def countAndVerify(self,suitelist,valuelist):
		c = []
		diff = []
		for i in range(len(valuelist)-1):
			c.append(valuelist.count(valuelist[i]))	
			if(i>=1):
				if (c[i]>=c[i-1]):
					v = valuelist[i]
						 	
			if( valuelist[i]+1 == valuelist[i+1]):
				diff.append(valuelist[i+1] - valuelist[i])		
				if (i==3 and sum(diff)==4 and diff.count(diff[1])==4):
					return i,v
			if(i==3):
				return c,v


