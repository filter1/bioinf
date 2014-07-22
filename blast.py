p = 'agttacag' # pattern
data = 'aaaaaagatt' # data
w = 5 # length of seeds
t = 5 # threshold for seeds 
c = 0 # threshold for hits
v = 3 # number of results

match = 2
mismatch = -3

class Hit:
	begin_pat = 0
	end_pat = 0
	begin_data = 0
	end_data = 0

	score = 0

	def __init__(self, begin_pat, end_pat):
		self.begin_pat = begin_pat
		self.end_data = end_data

	def get_score():
		data_s = data[begin:end]
		score = 0

		for s in seq:
			if s == data_s:
				score += match
			else:
				score += mismatch

	def extend_left():
		if begin <= 0:
			return - 1



seeds = []
for x in range(0, len(p) - w + 1):
	seeds.append(p[x: x + w])

print '1. Getting Seeds: ' + str(seeds)

for s in data:
	data.find(s)
