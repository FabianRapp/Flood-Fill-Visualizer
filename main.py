import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, TextBox
import gen_map as map
import init_main as init
import globals as g
import main_utils as u
import gen_map_globals as map_g

def fill_cell(tab, cur, fig, ax, size):
	for recusive_call, filled in zip (g.recursive_order, g.filled_state):
		tab[cur[1], cur[0]] = filled
		u.display_area(fig, ax, tab)
		if recusive_call == g.up:
			fill(tab, size, (cur[0], cur[1] - 1), fig, ax)
		elif recusive_call == g.down:
			fill(tab, size, (cur[0], cur[1] + 1), fig, ax)
		elif recusive_call == g.left:
			fill(tab, size, (cur[0] - 1, cur[1]), fig, ax)
		elif recusive_call == g.right:
			fill(tab, size, (cur[0] + 1, cur[1]), fig, ax)
	tab[cur[1], cur[0]] = g.filled_state[-1]
	u.display_area(fig, ax, tab)

def fill(tab, size, cur, fig, ax):
	original_value = tab[cur[1], cur[0]]
	tab[cur[1], cur[0]] = g.checking_color
	u.display_area(fig, ax, tab)
	tab[cur[1], cur[0]] = original_value
	if u.do_not_fill_color(tab, cur):
		return
	elif original_value == 1:
		fill_cell(tab, cur, fig, ax, size)

def flood_fill(tab, size, begin, fig, ax):
	begin = tuple(value + 1 for value in begin)
	fill(tab, size, begin, fig, ax)  # Start filling with 'to fill' as 1

def main():
	map.update_map()
	plt.close('all')
	size = (map_g.x_size, map_g.y_size)
	area = u.make_area(size)
	fig, ax = init.display_area(size)
	speed_slider = init.speed_slider()
	ax_legend = init.legend(fig)
	flood_fill(area, size, map_g.begin, fig, ax)
	plt.ioff()
	plt.show()

if __name__ == "__main__":
	main()
