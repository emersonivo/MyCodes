class bola():
	import re
	import os
	import glob

	from collections import defaultdict

	global block
	global tmp
	global homedir
	global lastcel
	global board

	block = defaultdict(list)
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
		import csv
		print("getdiag")
		for l in range(1, numlin + 1):
			for c in range(1, numcol + 1):
				pos = str(l)+str(c)
				if l == 1 and c == 1:
					cel = []
					for p in range(11, lastcel, 11):
						#cel.append(p)
						block["D_" + str(11)].append(p)
					#print("d11", cel)
				# elif l == 1 and c >= 1:
				# 	beg = int(str(l)+str(c))
				# 	end = lastcel + 10 - (c * 10)
				# 	cel = []
				# 	for p in range(beg, end, 11):
				# 		#cel.append(p)
				# 		block["D_" + str(beg)].append(p)
				# 	#print("diags" + str(beg), cel)
				# elif l >= 1 and c == 1:
				# 	beg = int(str(l)+str(c))
				# 	end = int(str(c)+str(l)) - 1
				# 	cel = []
				# 	for p in range(beg, end, - 9):
				# 		#cel.append(p)
				# 		block["D_" + str(beg)].append(p)
				# 	#print("diags" + str(beg), cel)
				# elif l >= 1 and c == numcol:
				# 	beg = int(str(l)+str(c))
				# 	end = int(str(c)+str(l)) + 1
				# 	cel = []
				# 	for p in range(beg, end, 9):
				# 		#cel.append(p)
				# 		block["D_" + str(beg)].append(p)
				# 	#print("diags" + str(beg), cel)
				elif l == numlin and c >= 1:
					beg = int(str(l)+str(c))
					end = int(str(l -c)+str(l - 1))
					#end = int(str(c)+str(l)) - 1
					cel = []
					for p in range(beg, end, - 11):
						#cel.append(p)
						block["D_" + str(beg)].append(p)
					#print("diags" + str(beg), cel)

		w = csv.writer(open("output.csv", "w"))
		for key, val in block.items():
			w.writerow([key, val])

	def getlines():
		import csv
		print("getlines")
		for l in range(1, numlin + 1):
			cel = []
			for c in range(1, numcol + 1):
				cel.append(str(c) + str(l))
			block["L_" + str(l) + str(c)].append(cel)

		w = csv.writer(open("output.csv", "a"))
		for key, val in block.items():
			w.writerow([key, val])

	def getcolumns():
		import csv
		print("columns")
		for l in range(1, numlin + 1):
			cel = []
			for c in range(1, numcol + 1):
				cel.append(str(c) + str(l))
			block["C_" + str(c) + str(l)].append(cel)

bola.createboard(8, 8)
bola.getdiag()
#bola.getlines()
#bola.getcolumns()

#print("Exported: ", block)

# import csv
# w = csv.writer(open("output.csv", "w"))
# for key, val in block.items():
#     w.writerow([key, val])


import csv
dict = {}
for key, val in csv.reader(open("output.csv")):
   dict[key] = val

#print("Imported: ", dict)

class newclass():
	def testadic():
		mydict = dict
		myval = "72"
		for y in mydict.values():
			#print("Y", y)
			if myval in y:
				print(y)
			#else:
			#	print("Aqui não tem ", myval, y)


newclass.testadic()