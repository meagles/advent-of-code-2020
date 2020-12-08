import re #regex

def open_puzzle_input(day):
    with open('./Day{}/input.txt'.format(day), 'r') as file:
        data = file.read()
        splitData = data.splitlines()
        return splitData

if __name__ == "__main__":

	day = 8
	puzzle = 2

	input = open_puzzle_input(day)

	if day == 8:
		if puzzle == 2:
			# we're gonna try this with slightly modified inputs until we get an answer
			for index_to_modify in range(len(input)):
				if input[index_to_modify][0:3] != "acc":
					# print("Trying with changed row "+str(index_to_modify+1))
					this_input = input.copy()
					line_to_modify = this_input[index_to_modify]
					if line_to_modify[:3] == "jmp":
						modified_line = "nop"+line_to_modify[3:len(line_to_modify)]
					elif line_to_modify[:3] == "nop":
						modified_line = "jmp"+line_to_modify[3:len(line_to_modify)]
					this_input[index_to_modify] = modified_line

					keep_running = True
					accumulator = 0
					current_row = 0
					executed_rows = []

					while keep_running:
						if current_row > len(this_input) or current_row in executed_rows:
							# print("+ infinite loop or out of bounds.")
							break
						elif current_row == len(this_input):
							print("Found infinite loop fix! Changed row "+str(index_to_modify+1))
							keep_running = False
							break
						else:
							executed_rows.append(current_row)
						line = this_input[current_row]
						# print("Running row "+str(current_row)+": "+line)
						line_parts = line.split(" ")
						if line_parts[0] == "acc":
							accumulator = accumulator + int(line_parts[1])
							current_row = current_row + 1
						elif line_parts[0] == "jmp":
							current_row = current_row + int(line_parts[1])
						elif line_parts[0] == "nop":
							current_row = current_row + 1
							continue
					if not keep_running:
						print("++++++Accumulator is at "+str(accumulator))

		elif puzzle == 1:
			print('aoeu')
			keep_running = True
			accumulator = 0
			current_row = 0
			executed_rows = []

			while keep_running:
				line = input[current_row]
				print("Running row "+str(current_row)+" (accumulator at "+str(accumulator)+"): "+line)
				if current_row in executed_rows:
					break
				else:
					executed_rows.append(current_row)
				line_parts = line.split(" ")
				if line_parts[0] == "acc":
					accumulator = accumulator + int(line_parts[1])
					current_row = current_row + 1
				elif line_parts[0] == "jmp":
					current_row = current_row + int(line_parts[1])
				elif line_parts[0] == "nop":
					current_row = current_row + 1
					continue
			print("Accumulator is at "+str(accumulator))
				
			
		

	elif day == 7:
		# create rules dictionary
		rules = {}
		for line in input:
			line_parts = line.split(" bags contain ")
			outer_color = line_parts[0]
			inner_colors = line_parts[1].split(', ')
			rules[outer_color] = {}
			for this_bag in inner_colors:
				num_color = this_bag[0:(this_bag.find(' bag'))]
				inner_color = num_color.lstrip('1234567890 ')
				inner_number = num_color.split(" ")[0]
				if inner_number == 'no':
					inner_number = 0
				rules[outer_color][inner_color] = int(inner_number)

		# create 
		
		def check_bag_contains(rules, outer_color, desired_color, seen_colors=[]):
			contents_dict = rules[outer_color]
			for this_color in contents_dict:
				if this_color == "no other":
					return False
				elif this_color == desired_color:
					return True
				elif this_color not in seen_colors: 
					# not the color we are looking for, but could it contain that color?
					if check_bag_contains(rules, this_color, desired_color, seen_colors):
						return True
					else:
						seen_colors.append(this_color)
			return False

		def count_bag_contents(rules, this_bag_color):
			num_bags = 1 # we have this bag at least
			contents_dict = rules[this_bag_color]
			for color in contents_dict:
				if color == "no other":
					return num_bags
				else:
					num_outer_bags = contents_dict[color]
					num_inner_bags = count_bag_contents(rules, color)
					num_bags = num_bags + (num_outer_bags * num_inner_bags)
			return num_bags

		if puzzle == 1:
			# look for shiny gold in each bag
			num_valid = 0
			for bag_color in rules:
				if check_bag_contains(rules, bag_color, 'shiny gold'):
					num_valid = num_valid + 1
					print(bag_color+" is valid")

			print("Total valid: "+str(num_valid))
		elif puzzle == 2:
			gold_bag_contents = count_bag_contents(rules, 'shiny gold') - 1 # don't count the gold bag
			print("Gold bag contains "+str(gold_bag_contents)+" bags")

	elif day == 6:
		group_yeses = ''
		answer_sum = 0
		new_group = True
		for line in input:
			if len(line) == 0:
				answer_sum = answer_sum + len(group_yeses)
				group_yeses = ''
				new_group = True
				continue
			if puzzle == 1:
				group_yeses = ''.join(set(group_yeses+line))
			elif puzzle == 2:
				if new_group:
					new_group = False
					group_yeses = line # at this point everyone has said yes
					continue
				else:
					personset = set(line)
					new_group_yeses = ''
					for char in group_yeses:
						if char in personset:
							new_group_yeses = new_group_yeses + char
					group_yeses = new_group_yeses
		
		answer_sum = answer_sum + len(group_yeses) # last set
		print("Sum: "+str(answer_sum))

	elif day == 5:
		highest_seat_id = 0
		all_seat_ids = []
		for line in input:
			front_back_info = line[0:7]
			left_right_info = line[7:10]
			front_back_binary = ""
			left_right_binary = ""
			for pos in range(7):
				if front_back_info[pos] == "F":
					front_back_binary += "0"
				elif front_back_info[pos] == "B":
					front_back_binary += "1"
			for pos in range(3):
				if left_right_info[pos] == "L":
					left_right_binary += "0"
				elif left_right_info[pos] == "R":
					left_right_binary += "1"
			row = int(front_back_binary,2)
			column = int(left_right_binary,2)
			seat_id = row * 8 + column
			all_seat_ids.append(seat_id)
			if seat_id > highest_seat_id:
				highest_seat_id = seat_id
		print("Highest seat id is: "+str(highest_seat_id))

		prev_seat_id = None
		for this_seat_id in sorted(all_seat_ids):
			if prev_seat_id is not None and this_seat_id != prev_seat_id + 1:
				print("We have seats "+str(this_seat_id)+" and "+str(prev_seat_id)+" with a seat between them")
			prev_seat_id = this_seat_id

	elif day == 4:
		def validate_passport(puzzle, passport_fields, passport_data):
			required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
			missing_fields = [field for field in required_fields if field not in passport_fields]
			if len(missing_fields) == 0 or missing_fields == ["cid"]:
				if puzzle == 1:
					return True
				else:
					for index in range(len(passport_fields)):
						this_data = str(passport_data[index])
						this_field = passport_fields[index]
						if this_field == 'byr' and (len(this_data) != 4 or int(this_data) < 1920 or int(this_data) > 2002):
							print('byr')
							return False
						elif this_field == 'iyr' and (len(this_data) != 4 or int(this_data) < 2010 or int(this_data) > 2020):
							print('iyr')
							return False
						elif this_field == 'eyr' and (len(this_data) != 4 or int(this_data) < 2020 or int(this_data) > 2030):
							print('eyr')
							return False
						elif this_field == 'hgt':
							print('hgt')
							if not re.search("^([0-9]+(cm|in))", this_data):
								return False
							if this_data.find('cm') != -1: # dealin' with metric
								number_centimeters = int(this_data[0:this_data.find('cm')])
								if number_centimeters < 150 or number_centimeters > 193:
									return False
							else: # dealin' with imperialism	
								number_inches = int(this_data[0:this_data.find('in')])
								if number_inches < 59 or number_inches > 76:
									return False
						elif this_field == 'hcl' and not re.search("^#([a-f0-9]{6})", this_data):
							print('hcl')
							return False
						elif this_field == 'ecl' and this_data not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
							print('ecl')
							return False
						elif this_field == 'pid' and (len(this_data) != 9 or not int(this_data)):
							print('pid')
							return False
					return True
			else: 
				return False

		valid_passports = 0
		passport_fields = []
		passport_data = []
		for row_num in range(0, len(input)+1):
			if row_num >= len(input): # we need an empty line at the end lol
				line = ""
			else:
				line = input[row_num]
			if len(line) > 0: # line with data
				line_parts = line.split(' ')
				for pair in line_parts:
					key_value = pair.split(':')
					passport_fields.append(key_value[0])
					passport_data.append(key_value[1])
			else: # blank line, check old user, go to new user
				if validate_passport(puzzle, passport_fields, passport_data):
					valid_passports = valid_passports + 1
				passport_fields = []
				passport_data = []

		print(str(valid_passports)+" valid passports found")

	elif day == 3:
		if puzzle == 1:
			velocities = [[3,1]]
		elif puzzle == 2:
			velocities = [[1,1],[3,1],[5,1],[7,1],[1,2]]
			mult_product = 1

		for velocity in velocities:
			x_pos = 0
			y_pos = 0
			x_vel = velocity[0]
			y_vel = velocity[1]
			print("Doing velocity: "+str(x_vel)+","+str(y_vel))
			trees_encountered = 0
			for row_num in range(0, len(input), y_vel):
				line = input[row_num]
				if x_pos >= len(line):
					x_pos = x_pos - len(line)
				if line[x_pos] == "#":
					trees_encountered = trees_encountered + 1
				x_pos = x_pos + x_vel
			if puzzle == 2:
				mult_product = mult_product * trees_encountered
			print(str(trees_encountered)+" trees encountered")
		if puzzle == 2:
			print("Multiplied product: "+str(mult_product))

	elif day == 2:
		valid_passwords = 0
		for line in input:
			line_parts = line.split(' ')
			pw_policy_parts = line_parts[0].split('-') # array of 2 values
			char = line_parts[1][0]
			password = line_parts[2]
			if puzzle == 1:
				char_count = password.count(char)
				min_char_count = int(pw_policy_parts[0])
				max_char_count = int(pw_policy_parts[1])
				if (char_count >= min_char_count and char_count <= max_char_count):
					valid_passwords = valid_passwords + 1
			elif puzzle == 2:
				position_1 = int(pw_policy_parts[0]) - 1 # they aren't 0-indexed, so policy char x is at python index x-1
				position_2 = int(pw_policy_parts[1]) - 1
				if (len(password) >= position_2): # check it's even long enough
					if ((password[position_1] == char and password[position_2] != char) or (password[position_2] == char and password[position_1] != char)):
						valid_passwords = valid_passwords + 1
		print(str(valid_passwords)+" passwords are valid")

	elif day == 1:
		if puzzle == 1:
			for line in input:
				for line2 in input:
					if (int(line)+int(line2))==2020:
						print("Result is "+str(int(line) * int(line2)))
		if puzzle == 2:
			for line in input:
				for line2 in input:
					for line3 in input:
						if (int(line)+int(line2)+int(line3))==2020:
							print("Result is "+str(int(line) * int(line2) * int(line3)))