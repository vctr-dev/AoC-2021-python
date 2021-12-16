from my_utils import draw

filename = 'input.txt'


def process_dot_line(l):
	[x, y] = l.split(',')
	return [int(x), int(y)]


def process_fold_line(l):
	[axis, line] = l.replace('fold along ', '').split('=')
	return [axis, int(line)]


def get_y(dot):
	return dot[1]


def get_x(dot):
	return dot[0]


def fold_x_axis(dots, line):
	for dot in [dot for dot in dots if get_x(dot) > line]:
		dots.remove(dot)
		dots.add((transform(get_x(dot), line), get_y(dot)))


def fold_y_axis(dots, line):
	for dot in [dot for dot in dots if get_y(dot) > line]:
		dots.remove(dot)
		dots.add((get_x(dot), transform(get_y(dot), line)))


def transform(coord, line):
	# line - distance from line
	return line - (coord - line)


data = open(filename).read()

[dots, folds] = data.split('\n\n')
dots = set([tuple(process_dot_line(l)) for l in dots.split('\n')])
folds = [process_fold_line(l) for l in folds.strip().split('\n')]

for [axis, line] in folds:
	if axis == 'x':
		fold_x_axis(dots, line)
	elif axis == 'y':
		fold_y_axis(dots, line)

draw.grid(dots, empty_char=' ')

