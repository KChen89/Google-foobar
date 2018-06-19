from fractions import gcd
import math
def answer(dimensions, your_position, guard_position, distance):
    # your code here
	my_pos, guard_pos=mirror_replication(dimensions, your_position, guard_position, distance)
	num_angles=find_angles(my_pos, guard_pos)
	return num_angles

def find_angles(my_pos, guard_pos):
	# find all possible angle 
	all_angle=dict()
	# check guard's coordinates
	for temp_pos in guard_pos:
		angle=cal_angle(temp_pos)
		dist=cal_dist(temp_pos)
		# store distance as value, angle as key
		if angle not in all_angle:
			all_angle[angle]=dist
		else:
			# if angle exists: preserve smaller distance
			if all_angle[angle]>dist:
				all_angle[angle]=dist
	# check my coordinates to avoid self-injury
	for temp_pos in my_pos:
		angle=cal_angle(temp_pos)
		dist=cal_dist(temp_pos)
		# if my angle is the same as guard's and 
		# my distance is larger than his: will self injury 
		# this will cover corner scenarios
		if angle in all_angle and dist<=all_angle[angle]:
			del all_angle[angle]
		
	return len(all_angle)
		
def cal_dist(pos):
	return math.sqrt(pos[0]**2+pos[1]**2)

def cal_angle(pos):
	# represent angle using numerator and denominator in tuple (hasable)
	if pos[0]==0:
		# 90 degree and cannot simplify
		pos_gcd=(pos[1], pos[0])
		return pos_gcd
	else:
		# use simplest format
		pos_gcd=gcd(abs(pos[0]), abs(pos[1]))
		return (pos[1]/pos_gcd, pos[0]/pos_gcd)

def check_distance(pos, distance):
	# check if pos to origin exceeds distance
	# or it is my position
	if cal_dist(pos)>distance or (pos[0]==0 and pos[1]==0):
		return False
	else:
		return True

def mirror_replication(dimensions, my_pos, guard_pos, distance):
	# calculate the guard and my locations in every mirrored replications
	# size of mirror replication just covers a circle center at my original 
	# location with radius of distance
	width=dimensions[0]
	height=dimensions[1]
	# number of replications needed on each direction to cover distance
	num_w=distance//width+1
	num_h=distance//height+1
	my_repl_pos=list()
	guard_repl_pos=list()
	# calculate my and guard's coordinates in each replication
	for i in range(-num_w, num_w+1):
		for j in range(-num_h, num_h+1):
			temp_my_pos, temp_guard_pos=pos_cal(i, j, width, height, my_pos, guard_pos)
			# check distance
			if check_distance(temp_my_pos, distance):
				my_repl_pos.append(temp_my_pos)
			if check_distance(temp_guard_pos, distance):
				guard_repl_pos.append(temp_guard_pos)
	return my_repl_pos, guard_repl_pos

def pos_cal(i, j, width, height, my_pos, guard_pos):
	# calculate mirror location given coordinates
	# assume origin is at left bottom corner of room
	if i%2==0 and j%2==0:
		i*=width
		j*=height
		# both even: no flip
		my_cord=[i,j]
		guard_cord=[i-my_pos[0]+guard_pos[0], j-my_pos[1]+guard_pos[1]]
	elif i%2!=0 and j%2!=0:
		i*=width
		j*=height
		# both odd: both up-down and left-right flip
		my_cord=[i-2*my_pos[0]+width, j-2*my_pos[1]+height]
		guard_cord=[i-my_pos[0]-guard_pos[0]+width, j-my_pos[1]-guard_pos[1]+height]
	elif i%2==0 and j%2!=0:
		i*=width
		j*=height
		# up-down flip
		my_cord=[i, j-2*my_pos[1]+height]
		guard_cord=[i-my_pos[0]+guard_pos[0], j-my_pos[1]-guard_pos[1]+height]
	elif i%2!=0 and j%2==0:
		i*=width
		j*=height
		# left-right flip
		my_cord=[i-2*my_pos[0]+width, j]
		guard_cord=[i-my_pos[0]-guard_pos[0]+width, j-my_pos[1]+guard_pos[1]]

	return my_cord, guard_cord

def unit_test(t,a,func):
	ta=func(*t)
	if ta!=a:
		print('Error: input {}. Output should be {} instead of {}'.format(t, a, ta))
	else:
		print('input {}, output {}. test case passed'.format(t, ta))

def test():
	inputs=[[[3,2], [1,1], [2,1], 4], 
	       [[300, 275], [150, 150], [185, 100], 500],
	       [[10, 10], [4, 4], [3, 3], 5000],
	       [[23, 10], [6, 4], [3, 2], 23]]
	ans=[7, 9, 739323, 8]
	for t,a in zip(inputs, ans):
		unit_test(t,a,answer)

if __name__ == '__main__':
	test()