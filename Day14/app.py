def find_floating_possibilities(binary_string_list, x_indices):
	if len(x_indices) > 0:
		this_index = x_indices.pop(0)
		binary_string_list_0 = binary_string_list.copy()
		binary_string_list_0[this_index] = '0'
		vals_from_0 = find_floating_possibilities(binary_string_list_0, x_indices.copy())
		vals_from_0.append(''.join(binary_string_list_0))

		binary_string_list_1 = binary_string_list.copy()
		binary_string_list_1[this_index] = '1'
		vals_from_1 = find_floating_possibilities(binary_string_list_1, x_indices.copy())
		vals_from_1.append(''.join(binary_string_list_1))

		return vals_from_0+vals_from_1
	else:
		return []

with open('./Day14/input.txt', 'r') as file:
	data = file.read()
	splitData = data.splitlines()

mask = None
memory_dict = {}
print("Part 1:")
for line in splitData:
	line_parts = line.split(" = ")
	if line_parts[0] == "mask":
		mask = line_parts[1]
		mask_digits = {}
		for index in range(len(mask)):
			if mask[index] != 'X':
				mask_digits[index] = mask[index]

	else:
		memory_address = int(line_parts[0][4:(len(line_parts[0])-1)])
		memory_bits_list = list(str(bin(int(line_parts[1])).replace("0b", "")).zfill(36))
		for index in mask_digits:
			memory_bits_list[index] = mask_digits[index]
		memory_dict[memory_address] = int(''.join(memory_bits_list), 2)

print("Sum of all memory: "+str(sum(memory_dict.values())))

print("Part 2:")
mask = None
memory_dict = {}
for line in splitData:
	line_parts = line.split(" = ")
	if line_parts[0] == "mask":
		mask = line_parts[1]
		change_to_1_digits = []
		float_digits = []
		for index in range(len(mask)):
			if mask[index] == '1':
				change_to_1_digits.append(index) # change to 1
			elif mask[index] == 'X':
				float_digits.append(index) # floating bit
	else:
		initial_memory_address = int(line_parts[0][4:(len(line_parts[0])-1)])
		memory_address_chars = list(str(bin(initial_memory_address).replace("0b", "")).zfill(36))
		memory_value = int(line_parts[1])
		for index in change_to_1_digits:
			memory_address_chars[index] = '1'
		floating_possibilities = find_floating_possibilities(memory_address_chars, float_digits)
		for memory_to_write in floating_possibilities:
			memory_dict[int(memory_to_write, 2)] = memory_value

print(memory_dict)
print("Sum of all memory: "+str(sum(memory_dict.values())))






