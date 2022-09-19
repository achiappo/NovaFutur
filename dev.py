
import argparse
import numpy as np

from scipy.spatial import distance

parser = argparse.ArgumentParser(
	prog='Z-city pizzas selection calculator',
	description='Calculate greatest pizza selection in city'
)

parser.add_argument(
	'--verbose',
	dest='verbose',
	action='store_true',
	help='argument to control verbosity of script'
)

args = parser.parse_args()

verbose = getattr(args, 'verbose')

## First step: read in the input information ##

if verbose:
	print('Insert Z-city grid size (N) and number of pizzerias (M)')

# clause to take into account wrongly inserted input
correct_grid_input = False

while not correct_grid_input:

	try:
		N, M = list( map(int, input().split()) )

		if N < 1 or N > 1000 or M < 1 or M > 1000 or N != int(N) or M != int(M):
			print('both N and M must be integers in the range [0, 1000]')
			continue

		else:
			correct_grid_input = True

			if verbose:
				print(f'\nYou have chosen a grid size of {N} and {M} pizzerias')

	except ValueError:
		print('input inserted erroneously! correct input example: 100 10')
		continue

# below is the code to flexibly read in the coordinates and distance to the blocks served by each pizzeria
if verbose:
	print("\nFor each pizzeria, please insert its coordinates X,Y and the number K of blocks it serves")

pizzerias_data = []

for m in range(M):

	correct_pizzeria_input = False

	while not correct_pizzeria_input:

		try:
			X, Y, K = list( map(int, input().split()) )

			if X < 1 or X > N:
				print(f'pizzeria coordinate X={X} must be in the range [1, {N}]')
				continue

			elif Y < 1 or Y > N:
				print(f'pizzeria coordinate Y={Y} must be in the range [1, {N}]')
				continue

			elif K < 1 or K > 1000:
				print(f'maximum delivery distance K={K} must be in the range [1, 1000]')
				continue

			else:
				pizzerias_data.append( [X, Y, K] )
				correct_pizzeria_input = True

		except ValueError:
			print('input inserted erroneously! correct input example: 24 58 12')
			continue


if verbose:
	print('\nYou have entered the following coordinates and delivery distance for each pizzeria:')
	print(f"{'N. pizzeria':<20}{'X coordinate':<20}{'Y coordinate':<20}{'K distance':<20}")

	for p, (x, y, k) in enumerate(pizzerias_data):
		print(f"{p+1:<20}{x:<20}{y:<20}{k:<20}")

## Second step: creating pizzerias serving map ##

# build grid of zeros to count pizzerias serving each city block
city_blocks = np.zeros( (N, N), dtype=int )

# create grid of 2D indices of blocks coordinates
city_grid_indices = np.dstack( np.indices( (N, N) ) ).reshape(-1, 2)

# consider pizzerias in turn
for x, y, k in pizzerias_data:

	# reduce by one unit to convert coordinates into (Python) array indices
	x -= 1
	y -= 1

	# calculate distances of subgrid blocks to pizzeria's location
	pizzeria_distances = distance.cdist(
		city_grid_indices, 
		[[x, y]], 
		metric='cityblock'
	).reshape(N, N)

	# increase count to blocks reached by pizzeria's delivery
	city_blocks[pizzeria_distances<=k] += 1

if verbose:
	print('\nThe city blocks delivery map is')
	for row in city_blocks[::-1]:
		print(' '.join(str(r) for r in row) )

max_selection = city_blocks.max()

# print to output the final answer
if verbose:
	print(f'\nThe greatest pizzas selection is: {max_selection}')
else:
	print(max_selection)
