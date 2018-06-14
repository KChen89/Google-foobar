def answers():
	pass

def unit_test(t,a,func):
	ta=func(t)
	if a!=ta:
		print('Error: input {}. Output should be {} instead of {}'.format(t, a, ta))
	else:
		print('test case passed')

def test():
	input=[]
	ans=[]
	for t,a in zip(input, ans):
		unit_test(t,a answers)

if __name__ == '__main__':
	test()