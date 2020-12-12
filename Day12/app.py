
part = 2

directions = ['S', 'W', 'N', 'E']
def turn_ferry(current_facing, turn_dir, turn_degrees):
	facing_index = directions.index(current_facing)
	if turn_dir == 'R':
		facing_index = int(facing_index + (turn_degrees/90)) % 4
	elif turn_dir == 'L':
		facing_index = int(facing_index - (turn_degrees/90)) % 4
	return directions[facing_index]

def move_ferry(current_pos, move_direction, speed):
	if (move_direction == 'F'):
		move_direction = current_facing
	facing_index = directions.index(move_direction)
		
	if (facing_index % 2) == 0: # north or south
		displacement = speed * (facing_index - 1)
		current_pos = (current_pos[0], current_pos[1] + displacement)
	else: # east or west
		displacement = speed * (facing_index - 2)
		current_pos = (current_pos[0] + displacement, current_pos[1])
	return current_pos

def turn_waypoint(current_vel, turn_dir, turn_degrees):
	if turn_dir == 'R':
		num_right_turns = int(turn_degrees/90) % 4
	elif turn_dir == 'L':
		num_right_turns = int(-1*turn_degrees/90) % 4

	if num_right_turns == 0:
		return current_vel
	elif num_right_turns == 1:
		return (current_vel[1], -1*current_vel[0])
	elif num_right_turns == 2:
		return (-1*current_vel[0], -1*current_vel[1])
	elif num_right_turns == 3:
		return (-1*current_vel[1], current_vel[0])

def change_velocity(current_vel, move_direction, amount):
	facing_index = directions.index(move_direction)
	if (facing_index % 2) == 0: # north or south
		acceleration = amount * (facing_index - 1)
		current_vel = (current_vel[0], current_vel[1] + acceleration)
	else: # east or west
		acceleration = amount * (facing_index - 2)
		current_vel = (current_vel[0] + acceleration, current_vel[1])
	return current_vel

with open('./Day12/input.txt', 'r') as file:
	data = file.read()
	splitData = data.splitlines()
	current_pos = (0, 0)
	if part == 1:
		current_facing = 'E'
	elif part == 2:
		current_vel = (10, 1)
	for line in splitData:
		order = line[0]
		amount = int(line[1:])
		if part == 1:
			if order in ['L', 'R']:
				current_facing = turn_ferry(current_facing, order, amount)
			else:
				current_pos = move_ferry(current_pos, order, amount)
		elif part == 2:
			if order in ['L', 'R']:
				current_vel = turn_waypoint(current_vel, order, amount)
			elif order == 'F':
				current_pos = (current_pos[0] + (amount * current_vel[0]), current_pos[1] + (amount * current_vel[1]))
			else:
				current_vel = change_velocity(current_vel, order, amount)
	print(current_pos)
	print(abs(current_pos[0]) + abs(current_pos[1]))
		
