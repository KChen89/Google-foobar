def answer(n):
	if len(n)>32:
		n=long(n)
	else:
		n=int(n)
	return even_divide(n, 0)

def even_divide(n, step):
	if n==0:
		return step
	if n==2:
		return step+1
	while n%2==0:
		n>>=1
		step+=1
	return odd_divide(n, step)

def odd_divide(n, step):
	if n==1:
		return step
	if n==3:
		return step+2
	# low=even_divide(n-1, step+1)
	# high=even_divide(n+1, step+1)
	val=compareDepth(n)
	return even_divide(val, step+1)
	

def compareDepth(n):
	p=n+1
	q=n-1
	while True:
		if p%2==0 and q%2!=0:
			return n+1
		elif p%2!=0 and 1%2==0:
			return n-1
		elif p%2!=0 and q%2!=0:
			return n-1
		else:
			p>>=1
			q>>=1
	raise AssertionError('This branch should not be reached')

def unit_test(t,a,func):
	ta=func(t)
	if a!=ta:
		print('Error: input {}. Output should be {} instead of {}'.format(t, a, ta))
	else:
		print('input {}, output {}. test case passed'.format(t, ta))

def test():
	input=['0', '1', '2', '3', '4', '5', '6', '7', '8', '11', '12', '13', '15', \
	      '16', '17', '14', '30', '60', '62', '63', '23']
	ans = [ 0,   0,   1,   2,   2,   3,   3,   4,   3,    5,    4,    5,    5,   \
	        4,    5,    5,    6,    7,    7,    7, 6]
	for t,a in zip(input, ans):
		unit_test(t, a, answer)

if __name__ == '__main__':
	test()
# def strNumTimesTwo(numStr):
# 	digit=len(numStr)
# 	for i in range(digit-1,-1,-1):
