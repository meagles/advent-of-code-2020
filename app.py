def open_puzzle_input(day):
    with open('./Day{}/input.txt'.format(day), 'r') as file:
        data = file.read()
        splitData = data.splitlines()
        return splitData

if __name__ == "__main__":

	day = 2
	puzzle = 2

	input = open_puzzle_input(day)

	if day == 2:
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