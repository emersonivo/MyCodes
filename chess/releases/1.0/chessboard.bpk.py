class bola():
	import re
	import os
	import glob
	from collections import defaultdict

	global diag
	global lins
	global cols
	global tmp
	global homedir
	global lastcel
	global board

	diag = defaultdict(list)
	lins = defaultdict(list)
	cols = defaultdict(list)
	numlin = 0
	numcol = 0
	board = []
	homedir = "/bkp_local/MyCodes/chess"
	tmp = homedir + "/tmp"

	def createboard(x, y):
		global numlin
		global numcol
		global lastcel
		numlin = x
		numcol = y
		lastcel = int(str(x) + str(y)) + 1
		for l in range(1, numlin + 1):
			for c in range(1, numcol + 1):
				board.append(str(l)+str(c))
		print("chessboard", board)

	def getdiag():
		print("getdiag")
		for l in range(1, numlin + 1):
			for c in range(1, numcol + 1):
				pos = str(l)+str(c)
				if l == 1 and c == 1:
					cel = []
					for p in range(11, lastcel, 11):
						cel.append(p)
						diag["d" + str(11)].append(cel)
					#print("d11", cel)
				elif l == 1 and c >= 1:
					beg = int(str(l)+str(c))
					end = lastcel + 10 - (c * 10)
					cel = []
					for p in range(beg, end, 11):
						cel.append(p)
					diag["d" + str(beg)].append(cel)
					#print("diags" + str(beg), cel)
				elif l >= 1 and c == 1:
					beg = int(str(l)+str(c))
					end = int(str(c)+str(l)) - 1
					cel = []
					for p in range(beg, end, - 9):
						cel.append(p)
					diag["d" + str(beg)].append(cel)
					#print("diags" + str(beg), cel)
				elif l >= 1 and c == numcol:
					beg = int(str(l)+str(c))
					end = int(str(c)+str(l)) + 1
					cel = []
					for p in range(beg, end, 9):
						cel.append(p)
					diag["d" + str(beg)].append(cel)
					#print("diags" + str(beg), cel)
				elif l == numlin and c >= 1:
					beg = int(str(l)+str(c))
					end = int(str(l -c)+str(l - 1))
					#end = int(str(c)+str(l)) - 1
					cel = []
					for p in range(beg, end, - 11):
						cel.append(p)
					diag["d" + str(beg)].append(cel)
					#print("diags" + str(beg), cel)
		print(diag)

	def getlines():
		print("getlines")
		for l in range(1, numlin + 1):
			cel = []
			for c in range(1, numcol + 1):
					cel.append(str(l)+str(c))
			lins["L" + str(l) + str(c)].append(cel)
		print(lins)

	def getcolumns():
		print("columns")
		for l in range(1, numlin + 1):
			cel = []
			for c in range(1, numcol + 1):
					cel.append(str(c)+str(l))
			cols["C" + str(c) + str(l)].append(cel)
		print(cols)

bola.createboard(8, 8)
bola.getdiag()
bola.getlines()
bola.getcolumns()

newcols = cols
print("Fora de tudo", newcols)

