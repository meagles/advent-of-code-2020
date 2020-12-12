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


with open('./Day12/input.txt', 'r') as file:
	data = file.read()
	splitData = data.splitlines()
	current_facing = 'E'
	current_pos = (0, 0)
	for line in splitData:
		order = line[0]
		amount = int(line[1:])
		if order in ['L', 'R']:
			current_facing = turn_ferry(current_facing, order, amount)
		else:
			current_pos = move_ferry(current_pos, order, amount)
	print(current_pos)
	print(abs(current_pos[0]) + abs(current_pos[1]))
		
