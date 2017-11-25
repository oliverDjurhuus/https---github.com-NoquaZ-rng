
matrix2 = [
[
0, 0, 0, 0, 0, 0, 0, 0, 0
],
[
0, 0, 0, 0, 0, 0, 0, 0, 0
],
[
0, 0, 0, 0, 0, 0, 0, 0, 0
],
[
0, 0, 0, 0, 0, 0, 0, 0, 0
],
[
0, 0, 0, 0, 0, 0, 0, 0, 0
],
[
0, 0, 0, 0, 0, 0, 0, 0, 0
],
[
0, 0, 0, 0, 0, 0, 0, 0, 0
],
[
0, 0, 0, 0, 0, 0, 0, 0, 0
],
[
0, 0, 0, 0, 0, 0, 0, 0, 0
]
]

matrix = [
[
6, 0, 0, 4, 3, 0, 0, 8, 0
],
[
1, 0, 5, 0, 0, 0, 0, 4, 3
],
[
4, 0, 3, 0, 0, 8, 0, 5, 0
],
[
8, 0, 1, 7, 0, 0, 0, 6, 0
],
[
0, 0, 6, 2, 0, 5, 0, 0, 1
],
[
0, 0, 0, 0, 6, 8, 2, 3, 0
],
[
3, 8, 0, 6, 0, 2, 0, 0, 0
],
[
2, 0, 0, 0, 7, 0, 0, 1, 8 
],
[
0, 0, 4, 0, 5, 9, 0, 0, 6
]
]










def pretty_print_matrix(matrix):
	#print matrix
	print '---------------------------'
	for e in matrix:
		print e[0:3], " | " , e[3:6], " | " , e[6:9]
		#for t in e:
		#	print t, " ",
		#print ''
	print '---------------------------'
def transpose(matrix):
	#looping through all elements in upper triangle
	for i in range(1,9):
		for j in range(i):
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
	return matrix
def compare(matrix_1, matrix_2):
	difference = False
	for i in range(9):
		for j in range(9):
			if matrix_1[i][j] != matrix_2[i][j]:
				print "comparison difference at [", i, j, "] "
				print matrix_1[i][j], matrix_2[i][j]
				difference = True
	if difference:
		print "NOT EQUAL!"
	else:
		print "EQUAL!"


def search_no(matrix, pivot):
	positions = []
	for i in range(9):
		for j in range(9):
			if pivot == matrix[i][j] :
				positions.append((i,j))
	return positions

def search_all(matrix):
	all_positions = []
	for i in range(1,10):
		all_positions.append(search_no(matrix, i))
	return all_positions

def scanning(matrix, pivot):
	for row in matrix:
		for e in row:
			print "hi"

	print pivot


all_entry_positions = search_all(matrix)


def make_candidates(matrix):
	for i in range(9):
		for j in range(9):
			if matrix[i][j] == 0 :
				matrix[i][j] = [h for h in range(1,10)]
	return matrix

def window_duplicate_exclusion_scan(matrix):
	windows = []

	# Extracting each 3x3 window into one collecting 'windows'
	for i in range(3):
		for j in range(3):
			window = []
			for k in range(3):
				window.extend(matrix[i*3+k][3*j:3*j+3])
			windows.append(window)
	#print windows

	# Checking for duplicates in each 3x3 window
	for window in windows:
		entries = []
		candidates = []

		# First separating entries and candidates
		for element in window:
			if type(element) == int: # the element is an entry
				entries.append(element)
			else :
				candidates.append(element)

		# Comparing entries with candidates and removing any 
		# candidate that is a duplicate.
		for entry in entries:
			for candidate in candidates:
				for index in range(len(candidate)):
					if (entry == candidate[index]):
						candidate.pop(index)
						break
						
	# The candidates has now been updated which are directly referenced
	# to the original matrix. Hence, the matrix is already updated.

def line_exclusion(matrix):

	# Vertical exclusion
	for line in matrix:
		candidates = []
		entries = []
		for element in line:
			if type(element) == int:
				entries.append(element)
			else:
				candidates.append(element)
		for entry in entries:
			for candidate in candidates:
				for index in range(len(candidate)):
					if entry == candidate[index]:
						candidate.pop(index)
						break
		#print line

	# Horizontal exclusion
	transpose(matrix)
	for line in matrix:
		candidates = []
		entries = []
		for element in line:
			if type(element) == int:
				entries.append(element)
			else:
				candidates.append(element)
		for entry in entries:
			for candidate in candidates:
				for index in range(len(candidate)):
					if entry == candidate[index]:
						candidate.pop(index)
						break
		#print line
	transpose(matrix)


def line_add_new_entries(matrix):
	for line in matrix:
		for index in range(len(line)):
			if type(line[index]) == list and len(line[index]) == 1:
				line[index] = line[index][0]
	#return matrix


pretty_print_matrix(matrix)
pretty_print_matrix(make_candidates(matrix))

for i in range(5):
	#window_duplicate_exclusion_scan(matrix)
	line_exclusion(matrix)

	line_add_new_entries(matrix)

	print i, " ------------------"
	pretty_print_matrix(matrix)









