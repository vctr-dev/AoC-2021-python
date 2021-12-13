num_increases = 0
depths = [int(v.strip()) for v in open('input.txt', 'r')]
last = depths[0]
for l in depths[1:]:
	if l > last:
		num_increases += 1
	last = l
print(num_increases)
