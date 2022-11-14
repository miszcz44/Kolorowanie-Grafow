def KolorujZachlannie(macierz):
	n = len(macierz)
	tab = [-1] * n
	tab[0] = 0
	kolory = [False] * n
	for i in range(n):
		for j in range(n):
			kolory[j] = False
		for j in range(n):
			if (macierz[i][j] > 0 and tab[j] != -1):
				kolory[tab[j]] = True
		k = 0
		while kolory[k]:
			k += 1
		tab[i] = k
	return tab

plik = open("pumpum.txt", "r")

liczbaKrawędzi = int(plik.readline())

macierz = [[ 0 for i in range(liczbaKrawędzi) ] for j in range(liczbaKrawędzi) ]

for liniaPliku in plik:
	sąsiadująceKrawędzie = liniaPliku.split(" ")
	sąsiadująceKrawędzie[1] = sąsiadująceKrawędzie[1][:len(sąsiadująceKrawędzie[1]) - 1]
	#print(sąsiadująceKrawędzie)
	macierz[int(sąsiadująceKrawędzie[0])-1][int(sąsiadująceKrawędzie[1])-1] = 1
	# macierz[int(sąsiadująceKrawędzie[1])-1][int(sąsiadująceKrawędzie[0])-1] = 1

tab = KolorujZachlannie(macierz)
print("Węzeł\tKolor")
for i in range(0, liczbaKrawędzi):
    print(str(i + 1) + "\t" + str(tab[i]))