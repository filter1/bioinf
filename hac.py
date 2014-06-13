import math

def distance2D(p1, p2):
	a = p2[0] - p1[0]
	b = p2[1] - p1[1]
	return math.sqrt(a * a + b * b)

def distanceCluster(cluster1, cluster2):
	return distanceClusterSingleLinkage(cluster1, cluster2)
	# return distanceClusterCompleteLink(cluster1, cluster2)
	#return distanceClusterCompleteLinkage(cluster1, cluster2)


def distanceClusterSingleLinkage(cluster1, cluster2):
	res = 10000 # MAX

	for p1 in cluster1:
		for p2 in cluster2:
			d = distance2D(p1, p2)
			if d < res:
				res = d
	return res

def distanceClusterCompleteLinkage(cluster1, cluster2):
	res = -1 # MIN

	for p1 in cluster1:
		for p2 in cluster2:
			d = distance2D(p1, p2)
			if d > res:
				res = d
	return res


def distanceClusterCentroidLinkage(cluster1, cluster2):
	x1 = 0
	x2 = 0
	y1 = 0
	y2 = 0

	for p1 in cluster1:
		x1 += p1[0] 
		y1 += p1[1]

	for p2 in cluster2:
		x2 += p2[0] 
		y2 += p2[1]

	avg_p1 = (x1/len(cluster1), y1/len(cluster1))
	avg_p2 = (x2/len(cluster2), y2/len(cluster2))
	return distance2D(avg_p1, avg_p2)	


input = [(8, 9),(9, 8),(14, 9),(2.5, 6),(6, 4),(7, 5)]
clusters = []

print 'Input: ' + str(input) + '\n'

for i in input:
	clusters.append([i])

while len(clusters) != 1:
	temp_c1 = []
	temp_c2 = []
	temp_d = 10000 # MAX

	for c1 in clusters:
		for c2 in clusters:
			distance = distanceCluster(c1, c2)
			if distance < temp_d and c1 != c2:
				temp_c1 = c1
				temp_c2 = c2
				temp_d = distance

	print 'Merging ' + str(temp_c1) + ' and ' + str(temp_c2) + ' with a distance of ' + str(temp_d) 			

	clusters.remove(temp_c1)
	clusters.remove(temp_c2)
	temp_c1.extend(temp_c2)
	clusters.append(temp_c1)

	print str(clusters) + '\n'

