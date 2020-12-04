import re

def open_puzzle_input(day):
    with open('./Day{}/input.txt'.format(day), 'r') as file:
        data = file.read()
        splitData = data.splitlines()
        return splitData

if __name__ == "__main__":

	day = 4
	puzzle = 2

	input = open_puzzle_input(day)

	if day == 4:
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