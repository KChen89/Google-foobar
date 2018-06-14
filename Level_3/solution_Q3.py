def answer(m, f):
	'''
	binary tree will take too long
	'''
	# m or f less than one is impossible
	if m<1 or f<1:
		return 'impossible'
	# reverse the replication process to see if m==f==1 could be reached
	# if m==f!=1. impossible to reach initial condition.
	step=0
	while True:
		if m==f:
			if m==1:
				return step
			else:
				return 'impossible'
		elif m>f:
			m-=f 
			step+=1
		else:
			f-=m
			step+=1
	return step

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

if __name__ == '__main__':
	test()