
def check_for_neighbors(pos_x, pos_y, data):
	neighbors = 0
	neighbor_positions = [(pos_x-1, pos_y-1),(pos_x, pos_y-1),(pos_x+1, pos_y-1),
		(pos_x-1, pos_y),(pos_x+1, pos_y),
		(pos_x-1, pos_y+1),(pos_x, pos_y+1),(pos_x+1, pos_y+1)
	]
	for this_neighbor in neighbor_positions:
		if this_neighbor[0] < 0 or this_neighbor[1] < 0 or this_neighbor[0] > len(data[0])-1 or this_neighbor[1] > len(data)-1:
			continue
		elif data[this_neighbor[1]][this_neighbor[0]] == "#":
			neighbors = neighbors + 1
	return neighbors

with open('./Day11/input.txt', 'r') as file:
	data = file.read()
	splitData = data.splitlines()
	nextIterationData = splitData.copy()
	steady_state = False
	iterations = 0
	while not steady_state:
		iterations = iterations + 1
		print("Iteration "+str(iterations))
		rows = len(splitData)
		columns = len(splitData[0])
		nextIterationData = []
		for pos_y in range(rows):
			nextIterationData.append('')
			for pos_x in range(columns):
				seat_current_value = splitData[pos_y][pos_x]
				if (seat_current_value == '.'):
					nextIterationData[pos_y] += '.'
					continue # floor
				elif seat_current_value == 'L':
					if check_for_neighbors(pos_x, pos_y, splitData) == 0:
						# change to occupied
						nextIterationData[pos_y] += '#'
					else:
						nextIterationData[pos_y] += 'L'
				elif seat_current_value == '#':
					if check_for_neighbors(pos_x, pos_y, splitData) >= 4:
						# change to empty
						nextIterationData[pos_y] += 'L'
					else:
						nextIterationData[pos_y] += '#'
		if nextIterationData == splitData:
			steady_state = True
		else: 
			splitData = nextIterationData.copy()
	print(str(iterations)+" iterations")

	occupied_seats = 0
	for line in splitData:
		occupied_seats = occupied_seats + line.count('#')
	print(occupied_seats)
		