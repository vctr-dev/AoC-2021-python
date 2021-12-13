depths = [int(v.strip()) for v in open('input.txt', 'r')]
window_len = 3
num_increases = 0
for i in range(1, len(depths) - window_len + 1):
	if sum(depths[i:i + window_len]) > sum(depths[i - 1:i + window_len - 1]):
		num_increases += 1
print(num_increases)

