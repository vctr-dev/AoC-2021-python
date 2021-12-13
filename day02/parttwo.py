hor = 0
depth = 0
aim = 0
filename = 'input.txt'

def forward(mag):
	global hor, depth, aim
	hor += mag
	depth += aim * mag


def down(mag):
	global aim
	aim += mag


def up(mag):
	global aim
	aim -= mag
	

for [direction, mag] in [l.strip().split(" ") for l in open(filename)]:
	mag = int(mag)
	if direction == "forward":
		forward(mag)
	elif direction == "down":
		down(mag)
	elif direction == "up":
		up(mag)

print(hor*depth)
