#def meet(n):
#	a = [0]
#	b = [n]
#	for i in range(1,int(n/2)+1):
#		for x in range(1,3):
#			a = a+[a[-1]+x]
#			print(a)
N = 10
STEP = 4

def meet(a,b):
	if a>b:
		return 0
	if a==b:
		return 1
		
	cnt = 0
	for x in range(1,STEP):
		for y in range(1,STEP):
			cnt = cnt + meet(a+x, b-y)
	return cnt
		
if __name__ == "__main__":
#	meet(4)
	print(meet(0,11))