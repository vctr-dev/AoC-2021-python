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


def render_dots(dots):
	min_x = min([get_x(dot) for dot in dots])
	min_y = min([get_y(dot) for dot in dots])
	max_x = max([get_x(dot) for dot in dots])
	max_y = max([get_y(dot) for dot in dots])
	lines = []
	for x in range(min_x, max_x + 1):
		row = []
		for y in range(min_y, max_y + 1):
			row.append('#' if (x, y) in dots else ' ')
		lines.append(''.join(row))
	print('\n'.join(lines))


data = open(filename).read()

[dots, folds] = data.split('\n\n')
dots = set([tuple(process_dot_line(l)) for l in dots.split('\n')])
folds = [process_fold_line(l) for l in folds.strip().split('\n')]

for [axis, line] in folds:
	if axis == 'x':
		fold_x_axis(dots, line)
	elif axis == 'y':
		fold_y_axis(dots, line)

render_dots(dots)

