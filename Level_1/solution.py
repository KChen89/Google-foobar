import math
def answer(n):
	primeStrSize=0
	primeStr=''
	num=2
	while primeStrSize<n+5:
		if isPrime(num):
			primeStr+=str(num)
			primeStrSize+=len(str(num))


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

if __name__ == '__main__':
	testPrime()


