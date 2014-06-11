import math

def distance2D(p1, p2):
	return math.sqrt(p1 * p1 + p2 * p2)

def distanceCluster(cluster1, cluster2):
	res = 10000 # MAX

	for p1 in cluster1:
		for p2 in cluster2:
			d = distance2D(p1, p2)
			if d < res:
				res = d
	return res

input = [(8, 9),(9, 8),(14, 9),(2.5, 6),(6, 4),(7, 5)]
clusters = []

for i in input:
	clusters.append([i[0], i[1])

while len(clusters) != 1:
	temp_c1 = []
	temp_c2 = []
	temp_d = 10000 # MAX

	for c1 in clusters:
		for c2 in clusters:
			distance = distanceCluster(c1, c2)
			if distance < temp_d and distance != 0: # because it will compare the same points
				temp_c1 = c1
				temp_c2 = c2
				temp_d = distance

	clusters.remove(temp_c1)
	clusters.remove(temp_c2)
	clusters.append(temp_c1.extend(temp_c2))
	print clusters

