import numpy
import matplotlib
def poker(suitelist,valuelist):
	if (suitelist[0]==suitelist[1]==suitelist[2]==suitelist[3]==suitelist[4]):
		x = "samesuit"
		valuelist = valuelist
		what,lastvalue = compare(x,valuelist)
		#lastvalue = compare(x,valuelist)
		return what,lastvalue
	else:
		x = "Not Suit"
		what,lastvalue = compare(x,valuelist)
		return what,lastvalue
		
def compare(x,valuelist):
	print valuelist
	valuelist = valuelist
	if (x=="samesuit"):
		print 'in same suit'
		valuelist.sort()
		for i in range(len(valuelist)-1):
			print i
			a = valuelist[i]+1 
			print a
			print valuelist[i+1]
			if( a == valuelist[i+1]):
						if (i==4):
				
					
							return str(flush),max(valuelist)
	else:
		print 'not in same suit'
		count = 0
		c = []
		for i in range(len(valuelist)-1):
			count = valuelist.count(valuelist[i])
			c.append(count)	
		if(max(c)==3 and min(c)==2):
			return("Full House",max(valuelist))
		if(max(c)==4):
			return("Four of a kind",max(valuelist))
		if(max(c)==3):
			return("Three of a kind",max(valuelist))		
		if(max(c)==2 and sum(c)==5):
			return("Two Pair",max(valuelist))
		if(max(c)==2):
			return("One Pair",max(valuelist))
		
what,lastvalue = poker(['d','d','d','d','d'],[10,11,12,13,14])
