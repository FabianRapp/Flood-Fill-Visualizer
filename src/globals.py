import matplotlib.colors

color_dict = {
	-1: 'gray',
	0: 'red',
	1: 'green',
	2: 'yellow',
	3: 'lightblue',
	4: 'skyblue',
	5: 'dodgerblue',
	6: 'royalblue',
	7: 'navy',
}
min_val, max_val = 0, 0

out_of_bounds_color = -1
do_not_fill_col = 0
checking_color = 2
to_fill_color = 1
filled_state = [3, 4, 5, 6, 7]
cmap = matplotlib.colors.ListedColormap([color_dict[i] for i in color_dict])

up = 1
down = 2
left = 3
right = 4
recursive_order = [up, down, right, left]

pause_time = 0.2

pause_box = 0
