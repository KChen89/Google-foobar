def answers(total_lambs):
	mg=most_generous(total_lambs)
	ms=most_stingy(total_lambs)
	print('total lambes {}'.format(total_lambs))
	print('mg: {}'.format(mg))
	print('ms: {}'.format(ms))
	return ms-mg

def most_stingy(n):
	'''
	first and second lowest level get paid one lambs
	other level henchmen gets paid the sum of
	their subordinates and subordinate's subordinate's pay
	1,1,2,3,5,8,13, ... 
	'''
	prev_prev=1
	prev=1
	temp_sum=0
	num_henchmen=0
	while True:
		num_henchmen+=1
		if num_henchmen==1:
			temp_sum+=prev_prev
			
		elif num_henchmen==2:
			temp_sum+=prev

		else: # num_henchmen>2
			current=prev_prev+prev
			temp_sum+=current
			prev_prev=prev
			prev=current
		if temp_sum>n:
			break
	return num_henchmen-1

def most_generous(n):
	'''
	each henchmen gets paid twice of their immediate subordnates
	most jonior henchmen gets only one lambs
	1, 2, 4, 8, .... , 2^k
	'''
	temp_sum=0
	num_henchmen=0
	while True:
		temp_sum+=2**num_henchmen
		if temp_sum>n:
			break
		num_henchmen+=1
	return num_henchmen

def func_test():
	for n in range(17):
		print(str(n))
		print('mg: {}'.format(most_generous(n)))
		print('ms: {}'.format(most_stingy(n)))

def unit_test(t,a,func):
	ta=func(t)
	if a!=ta:
		print('Error: input {}. Output should be {} instead of {}'.format(t, a, ta))
	else:
		print('test case passed')

def test():
	input=[10, 143]
	ans=[1, 3]
	for t,a in zip(input, ans):
		unit_test(t, a, answers)

if __name__ == '__main__':
	test()