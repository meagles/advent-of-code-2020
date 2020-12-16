with open('./Day16/input.txt', 'r') as file:
	data = file.read()
	splitData = data.splitlines()

rules = splitData[0:20]
my_ticket = splitData[22]
nearby_tickets = splitData[25:]

# build rules
rule_dict = dict()
for rule in rules:
	ruleParts = rule.split(':')
	validRanges = ruleParts[1].split(' or ')
	validRanges_0 = validRanges[0].split('-')
	validRanges_1 = validRanges[1].split('-')
	rule_dict[ruleParts[0].replace(' ', '_')] = ((int(validRanges_0[0]), int(validRanges_0[1])), (int(validRanges_1[0]), int(validRanges_1[1])))

invalid_values = []
for ticket in nearby_tickets:
	ticket_vals = ticket.split(',')
	for value in ticket_vals:
		ticket_wholly_invalid = True
		for rule in rule_dict:
			int_val = int(value)
			if (int_val > rule_dict[rule][0][0] and int_val < rule_dict[rule][0][1]) or (int_val > rule_dict[rule][1][0] and int_val < rule_dict[rule][1][1]):
				ticket_wholly_invalid = False
				break
		if ticket_wholly_invalid:
			invalid_values.append(int_val)
print(invalid_values)
print(sum(invalid_values))
		



	