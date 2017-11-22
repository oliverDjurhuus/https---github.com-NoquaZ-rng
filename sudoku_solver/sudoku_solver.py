
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
		print e
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

def sample_space(matrix):
	for i in range(9):
		for j in range(9):
			if matrix[i][j] == 0 :
				matrix[i][j] = [h for h in range(1,10)]
	return matrix

print pretty_print_matrix(sample_space(matrix))

def window_duplicate_exclusion_scan(matrix):

	for i in range(3):
		for j in range(3):
			print "hi"
			print matrix[i*3:i*3+3][j*3:j*3+3]









window_duplicate_exclusion_scan(matrix)

def line_duplicate_exclusion_scan():
	return 0

#sample_space(all_entry_positions)

print pretty_print_matrix(matrix)
print pretty_print_matrix(search_all(matrix))
#print search_all(matrix)





















