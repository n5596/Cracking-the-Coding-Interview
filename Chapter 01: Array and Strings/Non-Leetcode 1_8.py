### If an element in a mxn matrix is 0, set its row and column to zero

def print_matrix(matrix):
	m = len(matrix)
	
	for i in range(m):
		print(matrix[i])
	return

def nullifyRows(matrix, i):
	n = len(matrix[0])
	
	for j in range(n):
		matrix[i][j] = 0
	return matrix

def nullifyCols(matrix, i):
	m = len(matrix)

	for j in range(m):
		matrix[j][i] = 0
	return matrix

print('Input number of rows(m) and number of columns(n):')
m = int(input())
n = int(input())

matrix = [[0 for j in range(n)] for i in range(m)]
print('Input mxn entries for the matrix:')

rows = []
cols = []

for i in range(m):
	for j in range(n):
		value = int(input())
		matrix[i][j] = value

		if value == 0:
			if i not in rows:
				rows.append(i)
			if j not in cols:
				cols.append(j)

print('Original Matrix')
print_matrix(matrix)

for i in rows:
	matrix = nullifyRows(matrix, i)

for i in cols:
	matrix = nullifyCols(matrix, i)

print('Changed Matrix')
print_matrix(matrix)
