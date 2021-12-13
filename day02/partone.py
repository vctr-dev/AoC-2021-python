hor = 0
depth = 0
filename = 'input.txt'

def forward(mag):
	global hor
	hor += mag


def down(mag):
	global depth
	depth += mag


def up(mag):
	global depth
	depth -= mag
	

for [direction, mag] in [l.strip().split(" ") for l in open(filename)]:
	mag = int(mag)
	if direction == "forward":
		forward(mag)
	elif direction == "down":
		down(mag)
	elif direction == "up":
		up(mag)

print(hor*depth)
