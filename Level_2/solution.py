def answer(x, y):
	'''
	calculate the right bottom number 
	(which is also the totoal numbers of element in traingle)
	size of each diagnial line is 1, 2, 3 ... until x+y-1
	sum =(1+x+y-1)*(x+y-1)/2 

	'''
	total_number=(x+y-1)*(x+y)/2
	x_y=total_number-y+1
	return str(x_y)

def unit_test(t, a, ta):
	if a!=ta:
		print('Error for input: {}, {}. Output should be {} instead of {}'.format(x, y, ans, test_ans))
	else:
		print('test case passed')

def test():
	test_case=[[1,1], [2,3], [3,2], [5,10]]
	ans=['1', '8', '9', '96']
	for t,a in zip(test_case, ans):
		ta=answer(t[0], t[1])
		unit_test(t, a, ta)
			
if __name__ == '__main__':
	test()