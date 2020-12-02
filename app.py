def open_puzzle_input(day):
    with open('./Day{}/input.txt'.format(day), 'r') as file:
        data = file.read()
        splitData = data.splitlines()
        return splitData

if __name__ == "__main__":

	day = 1
	puzzle = 2

	if day == 1:
		input = open_puzzle_input(day)
		if puzzle == 1:
			for line in input:
				for line2 in input:
					if (int(line)+int(line2))==2020:
						print(line)
						print(line2)
						print(int(line) * int(line2))
						exit()
		if puzzle == 2:
			for line in input:
				for line2 in input:
					for line3 in input:
						if (int(line)+int(line2)+int(line3))==2020:
							print(line)
							print(line2)
							print(line3)
							print(int(line) * int(line2) * int(line3))
							exit()