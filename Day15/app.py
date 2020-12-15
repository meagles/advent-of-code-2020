puzzle_input = [6,19,0,5,7,13,1]
numbers_spoken = []

# go_until = 2020
go_until = 30000000

last_index_spoken = dict()

for turn in range(0, go_until):
	# print("Turn "+str(turn))
	if turn < len(puzzle_input):
		spoken_this_turn = puzzle_input[turn]
	elif numbers_spoken[turn-1] in last_index_spoken.keys():
		# print(str(numbers_spoken[turn-1])+" has been spoken")
		prev_index = last_index_spoken[numbers_spoken[turn-1]]
		spoken_this_turn = (turn-1) - prev_index
	else:
		spoken_this_turn = 0

	if turn > 0:
		last_index_spoken[numbers_spoken[turn-1]] = turn - 1
	numbers_spoken.append(spoken_this_turn)
	# print(numbers_spoken)
	# print(last_index_spoken)
	# input('')
	if turn % 10000 == 0:
		print(turn)
		
print(spoken_this_turn)