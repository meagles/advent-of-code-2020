def get_mod_inverse(number, modulo):
	g, x, y = egcd(number, modulo)
	if g != 1:
		raise Exception('No modular inverse')
	else:
		return x % modulo

def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)

with open('./Day13/input.txt', 'r') as file:
	data = file.read()
	splitData = data.splitlines()

	bus_lines = splitData[1].split(',')
	print ("Part 1")
	earliest_departure = int(splitData[0])
	shortest_time = 10000
	return_line = 0
	for this_freq in bus_lines:
		if this_freq == 'x':
			continue
		else:
			this_freq = int(this_freq)
			if (this_freq - (earliest_departure % this_freq)) < shortest_time:
				return_line = this_freq
				shortest_time = (this_freq - (earliest_departure % this_freq))
				print("You will wait "+str(shortest_time)+" minutes for the "+str(return_line)+" bus")
				print(shortest_time * return_line)
	print("Part 2")
	# This implements the Chinese Remainder Theorem which I read about here: https://brilliant.org/wiki/chinese-remainder-theorem/
	a_vals = []
	n_vals = []
	index = 0
	for line in bus_lines:
		if line != 'x':
			n_vals.append(int(line))
			a_vals.append(int(line) - index)
		index = index + 1

	product_of_mods = 1
	for mod_val in n_vals:
		product_of_mods = product_of_mods * mod_val
	
	solution_sum = 0
	for i in range(len(n_vals)):
		mod_val = n_vals[i]
		y_val = product_of_mods // mod_val
		z_val = get_mod_inverse(y_val, mod_val)
		solution_sum = solution_sum + (a_vals[i] * y_val * z_val)
	print(int(solution_sum))
	print(product_of_mods)
	t_val = solution_sum % product_of_mods
	print("Solution is "+str(int(t_val)))