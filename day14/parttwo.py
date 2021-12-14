filename = 'input.txt'

[polymer_template, pair_insertion_rules] = open(filename).read().split('\n\n')

pair_insertion_rules = {
	source: dest
	for [source, dest] in
	[l.split(' -> ') for l in pair_insertion_rules.splitlines()]
}

polymer_template_in_pair = {}
for i in range(0, len(polymer_template)-1):
	pair = polymer_template[i:i+2]
	polymer_template_in_pair[pair] = polymer_template_in_pair.get(pair, 0) + 1

char_dict = {}
for c in polymer_template:
	char_dict[c] = char_dict.get(c, 0) + 1

for i in range(0, 40):
	new_polymer_template_in_pair = {}
	for (key, value) in polymer_template_in_pair.items():
		insert = pair_insertion_rules.get(key)
		if insert:
			new_polymer_template_in_pair[key[0] + insert] = new_polymer_template_in_pair.get(key[0] + insert, 0) + value
			new_polymer_template_in_pair[insert + key[1]] = new_polymer_template_in_pair.get(insert+key[1], 0) + value
			char_dict[insert] = char_dict.get(insert, 0) + value
		else:
			new_polymer_template_in_pair[key] = new_polymer_template_in_pair.get(key, 0) + value
	polymer_template_in_pair = new_polymer_template_in_pair

values = list(char_dict.values())
values.sort()
print(values[-1] - values[0])
