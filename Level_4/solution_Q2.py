from fractions import gcd
def answer(banana_list):
	# map this question to max bipartite matching 
	num_guard=len(banana_list)
	if num_guard<2:
		return 1
	pair_matrix=[[False for x in range(num_guard)] for y in range(num_guard)]
	for i in range(num_guard):
		for j in range(num_guard):
			# only need to check half of matrix
			if i<j: 
				pair_matrix[i][j]=is_inf(banana_list[i], banana_list[j])
				pair_matrix[j][i]=pair_matrix[i][j]
	pairing_guard=pairing(pair_matrix)
	num_pair=pairing_guard.max_pair()
	return num_guard-2*(num_pair//2)

def is_inf(n1, n2):
	# check if n1 and n2 could create infinity loops
	if n1<1 or n2<1:
		raise Exception('number of banana cannot be smaller than one')
	return not is_power2((n1+n2)/gcd(n1, n2))
	
def is_power2(num):
	if num==0:
		return True
	while num>2:
		if num%2==0:
			num/=2
		else:
			return False
	if num==2:
		return True
	else:
		return False

class pairing:
	# biparite matching
	def __init__(self, pair_matrix):
		self.pair_matrix=pair_matrix
		self.num_guard=len(self.pair_matrix)
		self.pair=[-1]*self.num_guard
		self.match=[-1]*self.num_guard

	def find_pair(self, guard, visited):
		# loop over all other guards
		for p in range(self.num_guard):
			# if can be paired and not been visited
			if self.pair_matrix[guard][p] and not visited[p]:
				visited[p]=True
				# current one not paired, just pair with this one
				if self.pair[p]==-1:
					self.pair[p]=guard
					return True
				# if paired, recursive find if current pair can find another pair
				if self.find_pair(self.pair[p], visited):
					self.pair[p]=guard
					return True
		# if cannot be paired
		return False

	def max_pair(self):
		num_pair=0
		# loop every guard and find if could be paired
		for guard in range(self.num_guard):
			# if can be paired, number of pair+1
			if self.find_pair(guard, [False]*self.num_guard):
				num_pair+=1
		return num_pair

	def max_match(self, indice, v):
		# find number of pair by recursion (too slow)
		visited=v[:]
		if indice==self.num_guard or len(visited)==self.num_guard:
			return 0
		else:
			skip=self.max_match(indice+1, visited)
			if indice in visited or self.pair[indice]==-1 or self.pair[indice] in visited:
				return skip
			else:
				visited.append(self.pair[indice])
				visited.append(indice)
				take=2+self.max_match(indice+1, visited)
				return max(skip, take)

def unit_test(t,a,func):
	ta=func(*t)
	if ta!=a:
		print('Error: input {}. Output should be {} instead of {}'.format(t, a, ta))
	else:
		print('input {}, output {}. test case passed'.format(t, ta))

def test():
	inputs=[[[1,1]], [[1,7,3,21,13,19]]]
	ans=[2, 0]
	for t,a in zip(inputs, ans):
		unit_test(t,a,answer)

def inf_test():
	inputs=[[1,1], [13, 3], [21,1], [7,3], [1,8], [1,5], [1,7], [19,7]]
	ans=[False, False, True, True, True, True, False, True]
	for t,a in zip(inputs, ans):
		unit_test(t,a,is_inf)

if __name__ == '__main__':
	test()