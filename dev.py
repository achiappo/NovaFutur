import numpy as np

from scipy.spatial import distance

## First step: read in the input information

print('Insert Z-city grid size (N) and number of pizzerias (M)')

# clause to take into account wrongly inserted input
correct_grid_input = False

while not correct_grid_input:

	try:
		N, M = list( map(int, input().split()) )

		if N < 1 or N > 1000 or M < 1 or M > 1000 or N != int(N) or M != int(M):
			print('both N and M must be integers in the range [0, 1000] -> please retry')
			continue
		else:
			print(f'you have chosen a grid size of {N} and {M} pizzerias')
			correct_grid_input = True

	except ValueError:
		print('input inserted erroneously! correct input example: 100 10')
		continue

# below is the code to flexibly read in the coordinates and distance to the blocks served by each pizzeria
print("For each pizzeria, please insert its coordinates X,Y and the number K of blocks it serves")

pizzerias_data = []

for m in range(M):

	correct_pizzeria_input = False

	while not correct_pizzeria_input:

		try:
			X, Y, K = list( map(int, input().split()) )

			if X < 1 or X > N:
				print(f'pizzeria coordinate X={X} must be in the range [1, {N}] -> please retry')
				continue

			elif Y < 1 or Y > N:
				print(f'pizzeria coordinate Y={Y} must be in the range [1, {N}] -> please retry')
				continue

			elif K < 1 or K > 1000:
				print(f'maximum delivery distance K={K} must be in the range [1, 1000] -> please retry')
				continue

			else:
				correct_pizzeria_input = True

		except ValueError:
			print('input inserted erroneously! correct input example: 24 58 12')
			continue

		pizzerias_data.append( [X, Y, K] )


print(f"{'N. pizzeria':<20}{'X coordinate':<20}{'Y coordinate':<20}{'K distance':<20}")

for p, (x, y, k) in enumerate(pizzerias_data):
	print(f"{p+1:<20}{x:<20}{y:<20}{k:<20}")

