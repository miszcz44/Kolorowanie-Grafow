def colorGreedy(matrix):
	n = len(matrix)
	tab = [-1] * n
	tab[0] = 0
	colors = [False] * n
	for i in range(n):
		for j in range(n):
			colors[j] = False
		for j in range(n):
			if matrix[i][j] > 0 and tab[j] != -1:
				colors[tab[j]] = True
		k = 0
		while colors[k]:
			k += 1
		tab[i] = k
	return tab


file = open("algor.txt", "r")

edge_number = int(file.readline())

matrix = [[0 for i in range(edge_number)] for j in range(edge_number)]

for line in file:
	neighbouring_edges = line.split(" ")
	neighbouring_edges[1] = neighbouring_edges[1][:len(neighbouring_edges[1]) - 1]
	# print(neighbouring_edges)
	matrix[int(neighbouring_edges[0])-1][int(neighbouring_edges[1])-1] = 1
	matrix[int(neighbouring_edges[1])-1][int(neighbouring_edges[0])-1] = 1

tab = colorGreedy(matrix)
print("Węzeł\tKolor")
for i in range(0, edge_number):
	print(str(i + 1) + "\t" + str(tab[i]))
