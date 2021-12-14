filename = 'input.txt'

[polymer_template, pair_insertion_rules] = open(filename).read().split('\n\n')

pair_insertion_rules = {
	source: dest
	for [source, dest] in
	[l.split(' -> ') for l in pair_insertion_rules.splitlines()]
}

for i in range(0, 10):
	new_string = ""
	for i in range(0, len(polymer_template) - 1):
		test = polymer_template[i:i+2]
		insert = pair_insertion_rules.get(test, pair_insertion_rules.get(test[::-1])) 
		new_string += test[0]
		if insert:
			new_string += insert
			
	polymer_template = new_string + polymer_template[-1]

char_dict = {}
for c in polymer_template:
	char_dict[c] = char_dict.get(c, 0) + 1
values = list(char_dict.values())
values.sort()
print(values[-1] - values[0])
