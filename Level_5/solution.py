from math import factorial
from fractions import gcd
def answer(w,h,s):
	# use Burnside's lemma to solve this problem
	unique_state=long(0)
	# generate all partitions of width and height
	p_width=comb_sum(w)
	p_height=comb_sum(h)

	for h_p in p_height:
		for w_p in p_width:
			h_cnt=unchanged_orbits(h_p)
			w_cnt=unchanged_orbits(w_p)
			# sum all unchanged orbits
			unique_state+=h_cnt*w_cnt*count_sum(h_p, w_p, s)
	# divided by R! and C!
	unique_state//=(factorial(w)*factorial(h))
	return str(unique_state)

def count_sum(hp, wp, s):
	# sum all unchanged matrices 
	temp_sum=0
	for i in hp:
		for j in wp:
			temp_sum+=gcd(i,j)
	return s**temp_sum

def partition_count(partition):
	# count number of occurance
	count=dict()
	for p in partition:
		if p in count.keys():
			count[p]+=1
		else:
			count[p]=1
	return count

def unchanged_orbits(partition):
	# calculate unchanged orbits given partition
	total=factorial(sum(partition)) # total number of permutations
	p_count=partition_count(partition)
	repeat=1
	for k,v in p_count.items():
		# k occurs v times, 
		# pick one from each of the k partition: k**v
		# permutation of k partition (k**v)*v!
		repeat*=(k**v*factorial(v))
	return total//repeat

def comb_sum(n):
	# generate all partitions of orbits
	ans=[]
	prev=[]
	util(n, prev, ans, 1)
	return ans

def util(n, prev, ans, index):
	# find all combination sum to n
	if sum(prev)==n:
		ans.append(prev)
		return 
	elif sum(prev)>n:
		return
	else:
		for i in range(index, n+1):
			temp=prev[:]
			temp.append(i)
			util(n, temp, ans, i)

def unit_test(t,a,func):
	ta=func(*t)
	if ta!=a:
		print('Error: input {}. Output should be {} instead of {}'.format(t, a, ta))
	else:
		print('input {}, output {}. test case passed'.format(t, ta))

def sum_test():
	for i in range(1,5):
		prev=list()
		ans=list()
		comb_sum(i, prev, ans, 1)
		print('{}: {}'.format(i, ans))


def test():
	inputs=[[2,2,2], 
	        [2,3,4]]
	ans=['7', '430']
	for t,a in zip(inputs, ans):
		unit_test(t,a,answer)

if __name__ == '__main__':
	test()