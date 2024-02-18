import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog
import init_gen_map as init
import gen_map_globals as g

def update_begin(new):
	if g.grid[g.begin[1], g.begin[0]] == 2:
		g.grid[g.begin[1], g.begin[0]] = 0
	elif g.grid[g.begin[1], g.begin[0]] == 3:
		g.grid[g.begin[1], g.begin[0]] = 1
	g.begin = new
	if g.grid[g.begin[1], g.begin[0]] == 0:
		g.grid[g.begin[1], g.begin[0]] = 2
	elif g.grid[g.begin[1], g.begin[0]] == 1:
		g.grid[g.begin[1], g.begin[0]] = 3

def resolve_fill_cell(pos):
	if g.grid[pos[1], pos[0]] == 0:
		g.grid[pos[1], pos[0]] = 1
	elif g.grid[pos[1], pos[0]] == 2:
		g.grid[pos[1], pos[0]] = 3

def resolve_not_fill_cell(pos):
	if g.grid[pos[1], pos[0]] == 1:
		g.grid[pos[1], pos[0]] = 0
	elif g.grid[pos[1], pos[0]] == 3:
		g.grid[pos[1], pos[0]] = 2

def clicked_cell(click_type, position):
	if position[0] >= 0 and position[1] >= 0 and position[0] < g.grid.shape[1] and position[1] < g.grid.shape[0]:
		if click_type == 1:  # Left click
			if g.grid[position[1], position[0]] == 1:
				update_begin(position)
			resolve_fill_cell(position)
		elif click_type == 3:  # Right click
			if g.grid[position[1], position[0]] == 0:
				update_begin(position)
			resolve_not_fill_cell(position)
		init.plot_grid()

def update_grid_size():
	g.grid = init.zero_grid(g.x_size, g.y_size)
	g.mat = init.plot_grid()
	init.key_hooks()

def ask_for_size():
	temp_x, temp_y = g.x_size, g.y_size
	try:
		g.x_size = simpledialog.askinteger("Input", "Enter width:", parent=g.map_root, minvalue=1, maxvalue=100)
		g.y_size = simpledialog.askinteger("Input", "Enter height:", parent=g.map_root, minvalue=1, maxvalue=100)
		update_grid_size()
	except:
		g.x_size = temp_x
		g.y_size = temp_y
		update_grid_size()
	g.begin = (g.x_size - 1, g.y_size - 1)

def main_update_map():
	g.map_root = tk.Tk()
	g.map_root.title("Setup Map")
	init.plot()
	resize_button = init.resize_button()
	instructions = init.instructions()
	finished_button = init.exit_ways()
	g.map_root.mainloop()

def update_map():
	update_begin(g.begin)
	main_update_map()
	if g.grid[g.begin[1], g.begin[0]] == 3:
		g.grid[g.begin[1], g.begin[0]] = 1
	if g.grid[g.begin[1], g.begin[0]] == 2:
		g.grid[g.begin[1], g.begin[0]] = 0

if __name__ == "__main__":
	update_map()
