import matplotlib.pyplot as plt
import numpy as np
import globals as g
import gen_map as map
import gen_map_globals as map_g

def small_pause():
	if g.pause_time < 0.1:
		plt.pause(g.pause_time)
		return True
	return False

def my_pause():
	if small_pause():
		return
	old_pause_time = g.pause_time
	progress = 0
	while progress < 100:
		if small_pause():
			return
		if old_pause_time != g.pause_time:
			progress = 0
			old_pause_time = g.pause_time
		time_to_pause = g.pause_time * 0.01 - 0.0001
		progress = progress + 1
		plt.pause(time_to_pause)

def display_area(fig, ax, area):
	ax.clear()
	ax.imshow(area, cmap=g.cmap, vmin=-1, vmax=len(g.color_dict)-2)
	ax.axis('off')
	plt.draw()
	my_pause()

def on_close(event):
	plt.close('all')
	exit(0)

def update_pause_time(val):
	g.pause_time = 10**val
	percentage = ((val - g.min_val) / (g.max_val - g.min_val)) * 100
	g.pause_box.set_val(f'{percentage:.0f}%')

def do_not_fill_color(tab, cur):
	value = tab[cur[1], cur[0]]
	if value in [do_not_fill_color, g.out_of_bounds_color] or value in g.filled_state:
		return True
	return False

def make_area(size):
	area = np.full((size[1] + 2, size[0] + 2), g.out_of_bounds_color, dtype=int)
	for i in range(1, size[1] + 1):
		for j in range(1, size[0] + 1):
			area[i, j] = 1 if map_g.grid[i - 1, j - 1] == 1 else 0
	return area
