from math import ceil

def conta(conto, C):
	caracteres, linhas = 0, 1
	for i in conto.split():
		if caracteres + len(i) <= C:
			caracteres += len(i) + 1
		else:
			caracteres = len(i) + 1
			linhas += 1
	return linhas

while True:
	try:
		N, L, C = map(int,input().split())
		conto = input()
		paginas = ceil(conta(conto, C) / L)
		print(paginas)
	except EOFError:
		break