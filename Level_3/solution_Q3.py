
def answer(m):
	'''
	solve absorbing Markov chain using FR where F=(I-Q)^-1
	'''
	mSize=len(m)
	numCol=len(m[0])
	if numCol!=mSize:
		raise AssertionError('Matrix is NOT square')
	terminalIndice=list()
	if not findTerminal(m, terminalIndice):
		raise AssertionError('No teriminal states')
	
	I, Q, R=mPartition(m, terminalIndice)
		

def findTerminal(matrix, terminalIndice):
	'''
	find terminal states and fill 1 in corresponding entry
	convert matrix into float format
	'''
	mSize=len(matrix)
	for i in range(mSize):
		rowSum=sum(matrix[i])
		if rowSum==0:
			# find terminal
			terminalIndice.append(i)
			matrix[i][i]=1.0
		else:
			matrix[i]=[float(x)/rowSum for x in matrix[i]]
	if len(terminalIndice)==0:
		return False
	else:
		return True

def mPartition(matrix, terminalIndice):
	'''
	partition matrix into I, Q, R, O (only generate I, R, and Q)
	'''
	numT=len(terminalIndice)
	mSize=len(matrix)

	stateIndice=[x for x in range(mSize) if x not in terminalIndice]
	print('state instance: {}'.format(stateIndice))
	I=[[1.0 if x==y else 0.0 for x in range(numT)] for y in range(numT)]
	Q=[[0 for x in range(mSize-numT)] for y in range(mSize-numT)]
	R=[[0 for x in range(numT)] for y in range(mSize-numT)]
	for i,isi in enumerate(stateIndice):
		for j,jsi in enumerate(stateIndice):
			Q[i][j]=matrix[isi][jsi]

	for i,isi in enumerate(stateIndice):
		for j,jsi in enumerate(terminalIndice):
			R[i][j]=matrix[isi][jsi]
	tempSum=0
	for temp in R:
		tempSum+=sum(temp)
	if tempSum==0:
		raise AssertionError('No path to teriminal states')
	else:
		return I, Q, R
			
def mInverse(m):
	pass

def mMult(m1, m2):
	pass

def mSub(m1, m2):
	# return m1-m2 given sizes are exactly the same
	if len(m1)!=len(m2):
		raise AssertionError('Error mSub: matrix height is different')
	if len(m1[0])!=len(m2[0]):
		raise AssertionError('Error mSub: matrix width is different')
	m=[[0.0 for x in range(len(m1[0]))] for y in range(len(m1))]
	for i in range(len(m1)):
		for j in range(m1[0]):
			m[i][j]=m1[i][j]-m2[i][j]
	return m

def unit_test(t,a,func):
	ta=func(t)
	if a!=ta:
		print('Error: input {}. Output should be {} instead of {}'.format(t, a, ta))
	else:
		print('input {}, output {}. test case passed'.format(t, ta))

def test():
	input=[[1,1], [2,1], [2,4], [4,7]]
	ans=[0, 1, 'impossible', 4]
	for t,a in zip(input, ans):
		unit_test(t, a, answer)

def func_test():
	m=[[0, 1, 0, 0, 0, 1],
		    [4, 0, 0, 3, 2, 0],
		    [0, 0, 0, 0, 0, 0],
		    [0, 0, 0, 0, 0, 0],
		    [0, 0, 0, 0, 0, 0],
		    [0, 0, 0, 0, 0, 0]]
	terminalIndice=list()
	findTerminal(m, terminalIndice)
	print('terminalIndice {}'.format(terminalIndice))
	
	I, Q, R=mPartition(m, terminalIndice)
	print('Q {}'.format(Q))
	print('R {}'.format(R))
	print('I {}'.format(I))

if __name__ == '__main__':
	func_test()