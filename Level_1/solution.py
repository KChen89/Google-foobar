import math
def answer(n):
	pass

def genPrimeN(n):
	if n<5:
		raise AssertionError('n cannot be smaller than 5')
	primeStrSize=0
	primeStr=''
	num=1
	while primeStrSize<n:
		num+=1
		if isPrime(num):
			primeStr+=str(num)
			primeStrSize+=len(str(num))
	return primeStr[n-5:n]

def isPrime(n):
	if n<2:
		return False
	for i in range(2, int(math.sqrt(n))+1):
		if n%i==0:
			return False
	return True

def testPrime():
	cnt=1
	p=0
	while p<10:
		if isPrime(cnt):
			p+=1
			print(str(cnt))
		cnt+=1

def testPrimeN(n):
	print(genPrimeN(n))

if __name__ == '__main__':
	# testPrime()
	testPrimeN(4+5)


