from fractions import Fraction, gcd
def answer(m):
	# solve absorbing Markov chain using FR where F=(I-Q)^-1
	mSize=len(m)
	numCol=len(m[0])
	# if numCol!=mSize:
	# 	raise Exception('Matrix is NOT square')
	if mSize==1:
		return [1,1]
	terminalIndice=list()
	findTerminal(m, terminalIndice)
	I, Q, R=mPartition(m, terminalIndice)
	IQ=mSub(I,Q)
	F=mInverse(IQ)
	FR=mMult(F, R)
	rawProb=FR[0]
	dnt=[x.denominator for x in rawProb]
	nmrt=[x.numerator for x in rawProb]
	lcmDnt=lcm(dnt)
	for i in range(len(nmrt)):
		nmrt[i]=nmrt[i]*lcmDnt/dnt[i]
	nmrt.append(lcmDnt)
	return nmrt

def lcm(inputs):
	tempLCM=None
	for temp in inputs:
		if tempLCM is None:
			tempLCM=temp
		else:
			tempLCM=tempLCM*temp//gcd(tempLCM, temp)
	return tempLCM
		
def findTerminal(matrix, terminalIndice):
	# find terminal states and fill 1 in corresponding entry
	# convert matrix into fraction format
	mSize=len(matrix)
	for i in range(mSize):
		rowSum=sum(matrix[i])
		if rowSum==0:
			# find terminal
			terminalIndice.append(i)
			matrix[i][i]=1.0
		else:
			matrix[i]=[Fraction(x, rowSum) for x in matrix[i]]
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
	# print('state instance: {}'.format(stateIndice))
	I=[[Fraction(1,1) if x==y else Fraction(0,1) for x in range(mSize-numT)] for y in range(mSize-numT)]
	Q=[[0 for x in range(mSize-numT)] for y in range(mSize-numT)]
	R=[[0 for x in range(numT)] for y in range(mSize-numT)]
	for i,isi in enumerate(stateIndice):
		for j,jsi in enumerate(stateIndice):
			Q[i][j]=matrix[isi][jsi]

	for i,isi in enumerate(stateIndice):
		for j,jsi in enumerate(terminalIndice):
			R[i][j]=matrix[isi][jsi]
	# tempSum=0
	# for temp in R:
	# 	tempSum+=sum(temp)
	# if tempSum==0:
	# 	raise AssertionError('No path to teriminal states')
	# else:
	return I, Q, R
			
def mInverse(m):
	h=len(m)
	w=len(m[0])
	idt=[[Fraction(1,1) if x==y else Fraction(0,1) for x in range(w)] for y in range(h)]
	# append idt to right side of m 
	for i in range(h):
		m[i]+=idt[i]
	# check along diagnoal line 
	for col in range(h):
		digonalScale(m, col)
		# make other rows at col zero 
		for row in range(h):
			if row!=col:
				rowScale(m, col, row)
	F=[]
	for temp in m:
		F.append(temp[w:])
	return F

def digonalScale(m, col):
	'''
	make diangoal one; if diagnoal is 0, find nearest row to swap; 
	if the entire col is zero, matrix is non-invertible
	'''
	if m[col][col]==0:
		fnz=findNonZero(m, col)
		if fnz is None:
			raise Exception('Matrix is non-invertible')
		m[col], m[fnz]=m[fnz], m[col]
	# scale m[col][col] to one
	scalar=m[col][col]
	m[col][col:]=[temp/scalar for temp in m[col][col:]]

def findNonZero(m, col):
	row=col
	while row<len(m):
		if m[row][col]!=0:
			return row
		row+=1
	return None

def rowScale(m, ref, oth):
	# make m[oth][ref]=0 by linear operation with m[ref][:]
	# if len(m)<max(ref, oth):
	# 	raise Exception('index is larger than matrix row')
	scalar=m[oth][ref]/m[ref][ref]
	# if len(m[ref])!=len(m[oth]):
	# 	raise AssertionError('oth {}, ref {}'.format(len(m[oth]), len(m[ref])))
	for index in range(len(m[oth])):
		m[oth][index]=m[oth][index]-scalar*m[ref][index]

def mMult(m1, m2):
	# multiple two matrix m1 and m2
	h1=len(m1)
	w1=len(m1[0])
	h2=len(m2)
	w2=len(m2[0])

	# if w1!=h2:
	# 	raise Exception('matrix size NOT match')
	product=[[0.0 for x in range(w2)] for y in range(h1)]
	for i in range(h1):
		for j in range(w2):
			product[i][j]=innerProduct(m1, i, m2, j)
	return product

def innerProduct(m1, row, m2, col):
	# compuate inner product of a row and column 
	# given two matrix and row and col num
	prod=0
	w=len(m1[0])
	h=len(m2)
	# if h!=w:
	# 	raise Exception('inner product: size NOT match')
	for i in range(h):
		prod+=m1[row][i]*m2[i][col]
	return prod

def mSub(m1, m2):
	# return m1-m2 given sizes are exactly the same
	# if len(m1)!=len(m2):
	# 	raise Exception('Error mSub: matrix height is different')
	# if len(m1[0])!=len(m2[0]):
	# 	raise Exception('Error mSub: matrix width is different')
	m=[[Fraction(0,1) for x in range(len(m1[0]))] for y in range(len(m1))]
	for i in range(len(m1)):
		for j in range(len(m1[0])):
			m[i][j]=m1[i][j]-m2[i][j]
	return m

def unit_test(t,a,func):
	ta=func(t)
	if not cmp(ta, a):
		print('Error: input {}. Output should be {} instead of {}'.format(t, a, ta))
	else:
		print('input {}, output {}. test case passed'.format(t, ta))

def cmp(ta, a):
	if len(ta)!=len(a):
		return False
	for i in range(len(ta)):
		if ta[i]!=a[i]:
			return False
	return True

def test():
	input=[[[0, 1, 0, 0, 0, 1],
	   [4, 0, 0, 3, 2, 0],
	   [0, 0, 0, 0, 0, 0],
	   [0, 0, 0, 0, 0, 0],
	   [0, 0, 0, 0, 0, 0],
	   [0, 0, 0, 0, 0, 0]],

	   [[0,2,1,0,0],
	   [0,0,0,3,4],
	   [0,0,0,0,0],
	   [0,0,0,0,0],
	   [0,0,0,0,0]]]
	ans=[[0,3,2,9,14],[7,6,8,21]]
	for t,a in zip(input, ans):
		unit_test(t, a, answer)

def func_test():
	m=[[0, 1, 0, 0, 0, 1],
	   [4, 0, 0, 3, 2, 0],
	   [0, 0, 0, 0, 0, 0],
	   [0, 0, 0, 0, 0, 0],
	   [0, 0, 0, 0, 0, 0],
	   [0, 0, 0, 0, 0, 0]]
	m=[[0,2,1,0,0],
	   [0,0,0,3,4],
	   [0,0,0,0,0],
	   [0,0,0,0,0],
	   [0,0,0,0,0]]
	terminalIndice=list()
	findTerminal(m, terminalIndice)
	print('terminalIndice {}'.format(terminalIndice))
	
	I, Q, R=mPartition(m, terminalIndice)
	IQ=mSub(I,Q)
	F=mInverse(IQ)
	print('matrix {}'.format(m))
	print('Q {}'.format(Q))
	print('R {}'.format(R))
	print('I {}'.format(I))
	print('I-Q {}'.format(IQ))
	print('Inverse I-Q {}'.format(F))
	FR=mMult(F, R)
	print('FR {}'.format(FR))
	rawProbability=FR[0]
	print('prob {}'.format(rawProbability))
	rawProb=FR[0]
	dnt=[x.denominator for x in rawProb]
	nmrt=[x.numerator for x in rawProb]
	lcmDnt=lcm(dnt)
	print('denonimator {}'.format(dnt))
	print('numerator {}'.format(nmrt))
	print('lcm {}'.format(lcmDnt))
	for i in range(len(nmrt)):
		nmrt[i]=nmrt[i]*lcmDnt/dnt[i]
	print('numerator {}'.format(nmrt))
	nmrt.append(lcmDnt)
	print('ans {}'.format(nmrt))


if __name__ == '__main__':
	test()