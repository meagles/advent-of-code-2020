def add_to_rule_poss(rule_name, mult_poss=['']):
	this_mult_poss = mult_poss.copy()
	# print("mult_poss = "+str(mult_poss))
	rule = rule_dict[rule_name]
	if len(rule) == 1:	# single possibility
		# print("look at rule "+rule_name+"="+str(rule)+": single")
		if rule[0] == ['"a"'] or rule[0] == ['"b"']:
			new_mult_poss = []
			for i in range(len(mult_poss)):
				new_mult_poss.append(mult_poss[i] + rule[0][0][1])
			return new_mult_poss
		else:
			for next_rule in rule[0]:
				mult_poss = add_to_rule_poss(next_rule, mult_poss)
				# print("after "+str(next_rule))
				# print(mult_poss)
			return mult_poss
	else: # multiple possibilities
		# print("look at rule "+rule_name+": multiple possibilities")
		return_mult_poss = []
		for this_rule in rule:
			# print("handle "+str(this_rule))
			new_mult_poss = mult_poss.copy()
			for this_rule_step in this_rule:
				new_mult_poss = add_to_rule_poss(this_rule_step, new_mult_poss)
				# print('new_mult_poss:')
				# print(new_mult_poss)
			return_mult_poss.extend(new_mult_poss)
			# print(return_mult_poss)
		return return_mult_poss
		
with open('./Day19/input.txt', 'r') as file:
	data = file.read()
	splitData = data.splitlines()
	rules = True
	rule_dict = dict()
	count = 0
	for line in splitData:
		if line == '':
			rules = False
			rule_0 = add_to_rule_poss('0')
			continue # or continue 
		elif rules:
			rule_parts = line.split(': ')
			rule_poss = rule_parts[1].split(' | ')
			for i in range(len(rule_poss)):
				rp = rule_poss[i].split(' ')
				rule_poss[i] = rp.copy()
			rule_dict[rule_parts[0]] = rule_poss
		else:
			if line in rule_0:
				count = count+1
print(count)


'''
for rule 91 (104 97) we would want our system to go
	mult_poss = ['']
	look at rule 104: multiple possibilities: 
		handle (2 2):
			look at rule 2:
				rule 2 = b, mult_poss = ['b']
			look at rule 2:
				rule 2 = b, mult_poss = ['bb']
		handle (97 2):
			look at rule 97:
				rule 97 = 'a', mult_poss = ['bb','a']
			look at rule 2:
				rule 2 = b, mult_poss = ['bb,'ab']
	mult_poss = ['bb','ab']
	look at rule 97: 
		rule 97 = 'a', mult_poss = ['bba','aba']


mult_poss = ['']
look at 76=(97 55 | 2 104): branches
	this_mult_poss = ['']
	handle (97 55):
		look at 97=a: single
			this_mult_poss = ['a']
		look at 55=(2 2): single
			this_mult_poss=['a']
			look at 2=b: single
				thies_mult_poss = ['ab']
			look at 2=b: single
				this_mult_poss = ['abb']
		this_mult poss = ['abb']
	handle (2 104):
		look at 2=b: single
			mult_poss = ['b']
		look at 104=(2 2 | 97 2): branches
			this_mult_poss = ['b']
			handle (2 2): 
				look at 2=b: single
					this_mult_poss = ['bb']
				look at 2=b: single
					this_mult_poss = ['bbb']
			handle (97 2):
				look at 97=a: single
					97=a, this_mult_poss = ['ba']
				look at 2=b: single
					this_mult_poss = ['bab']
			this_mult_poss = ['bbb','bab']
	this_mult_poss = ['abb', 'bbb', 'bab']
'''





