import numpy as np

from scipy.spatial import distance

## First step: read in the input information

print('Insert Z-city grid size (N) and number of pizzerias (M)')

# clause to take into account wrongly inserted input
correct_input = False

while not correct_input:

	try:
		N, M = list( map(int, input().split()) )

		if N < 0 or N > 1000 or M < 0 or M > 1000 or N != int(N) or M != int(M):
			print('both N and M must be integers in the range [0, 1000]. please reretry')
			continue
		else:
			print(f'you have chosen a grid size of {N} and {M} pizzerias')
			correct_input = True

	except ValueError:
		print('input inserted erroneously! correct input example: 100 10')
		continue

# below is the code to flexibly read in the coordinates and distance to the blocks served by each pizzeria
print("For each pizzeria, please insert its coordinates X,Y and the number K of blocks it serves")

pizzerias_data = []

for m in range(M):
	try:
		X, Y, K = list( map(int, input().split()) )
	except ValueError:
		print('input inserted erroneously! correct input example: 24 58 12')

	pizzerias_data.append( [X, Y, K] )

