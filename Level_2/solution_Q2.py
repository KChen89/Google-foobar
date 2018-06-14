def answers(total_lambs):
	mg=most_generous(total_lambs)
	ms=most_stingy(total_lambs)
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
	sub=0.5
	while True:
		temp_sum+=int(sub*2)
		if temp_sum>n:
			# check if remains can still pay one more after second level
			# if remains is greater than or equal to previous two subordinates' pay sum
			if num_henchmen>=1:
				rems=temp_sum-sub*2
				min_pay=sub+int(sub/2)
				if n-rems>=min_pay:
					num_henchmen+=1
				return num_henchmen
			else:
				return num_henchmen
		sub*=2
		num_henchmen+=1

def func_test():
	for n in range(30):
		print(str(n))
		print('mg: {}'.format(most_generous(n)))
		print('ms: {}'.format(most_stingy(n)))

def unit_test(t,a,func):
	ta=func(t)
	if a!=ta:
		print('Error: input {}. Output should be {} instead of {}'.format(t, a, ta))
	else:
		print('input {}, output {}. test case passed'.format(t, ta))

def test():
	input=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	ans = [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1]
	for t,a in zip(input, ans):
		unit_test(t, a, answers)

if __name__ == '__main__':
	func_test()