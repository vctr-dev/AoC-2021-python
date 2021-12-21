def parse(hex):
	return ''.join([bin(int(c, 16))[2:].zfill(4) for c in hex])


class Feed:
	def __init__(self, bin):
		self.feed = bin

	def __str__(self):
		return self.feed

	def __len__(self):
		return len(self.feed)

	def take(self, n):
		res = self.feed[0:n]
		self.feed = self.feed[n:]
		return res


class Packet:
	def __init__(self, version, type_id, value, sub_packets=[]):
		self.version = version
		self.type_id = type_id
		self.value = value
		self.sub_packets = sub_packets

	def __str__(self):
		sub_packets_str = ''
		if len(self.sub_packets):
			sub_packets_str = "\n\nSub-Packets\n\n" + '\n\n'.join(
				[str(p) for p in self.sub_packets]) + "\n\nEnd Sub-Packets"
		return "version: " + str(self.version) + "\ntype_id: " + str(
			self.type_id) + "\nvalue: " + str(self.value) + sub_packets_str


def make_packet(feed):
	version = int(feed.take(3), 2)
	type_id = int(feed.take(3), 2)
	if type_id == 4:
		return make_literal_packet(version, type_id, feed)
	length_type_id = feed.take(1)
	if length_type_id == '0':
		sub_packets_length = int(feed.take(15), 2)
		sub_packets_feed = Feed(feed.take(sub_packets_length))
		return make_length_operator_packet(version, type_id, sub_packets_feed)
	else:
		num_sub_packets= int(feed.take(11), 2)
		return make_num_sub_packets_operator_packet(version, type_id, feed, num_sub_packets)

def make_num_sub_packets_operator_packet(version, type_id, feed, num_sub_packets):
	packets = []
	for _ in range(0, num_sub_packets):
		packets.append(make_packet(feed))
	return Packet(version, type_id, None, packets)

def make_length_operator_packet(version, type_id, feed):
	packets = []
	while (len(feed)):
		packets.append(make_packet(feed))
	return Packet(version, type_id, None, packets)

def make_literal_packet(version, type_id, feed):
	bin = ''
	while (True):
		cont = feed.take(1)
		bin += feed.take(4)
		if cont == '0':
			break
	return Packet(version, type_id, int(bin, 2))

def gather_versions(packet):
	version = 0
	explore = [packet]
	while len(explore):
		p = explore.pop()
		version += p.version
		explore += p.sub_packets
	return version
# part two

def mul(iterables):
	res = 1
	for n in iterables:
		res *= n
	return res

def compute_packet(packet):
	if packet.type_id == 4:
		return packet.value
	sub_packets_res = [compute_packet(p) for p in packet.sub_packets]
	if packet.type_id == 0:
		return sum(sub_packets_res)
	if packet.type_id == 1:
		return mul(sub_packets_res)
	if packet.type_id == 2:
		return min(sub_packets_res)
	if packet.type_id == 3:
		return max(sub_packets_res)
	[first, second, *_] = sub_packets_res
	if packet.type_id == 5:
		return 1 if first > second else 0
	if packet.type_id == 6:
		return 1 if first < second else 0
	if packet.type_id == 7:
		return 1 if first == second else 0

input = open('input.txt').read().strip()

# part one examples
example0 = 'D2FE28'
example1 = '38006F45291200'
example2 = 'EE00D40C823060'
example3 = '8A004A801A8002F478'
example4 = '620080001611562C8802118E34'
example5 = 'C0015000016115A2E0802F182340'
example6 = 'A0016C880162017C3686B18A3D4780'


# part two examples
example_part_two = [('C200B40A82', 3), ('04005AC33890', 54), ('880086C3E88112', 7), ('CE00C43D881120', 9), 
('D8005AC2A8F0', 1),
('F600BC2D8F', 0),
('9C005AC2F8F0', 0),
('9C0141080250320F1802104A08', 1)]
for (inp, out) in example_part_two:
	feed = Feed(parse(inp))
	root_packet = make_packet(feed)
	print(compute_packet(root_packet) == out)

feed = Feed(parse(input))
root_packet = make_packet(feed)
print(compute_packet(root_packet))
