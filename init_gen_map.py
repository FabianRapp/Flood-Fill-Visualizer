import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import numpy as np
import gen_map_globals as g
import gen_map

def plot_grid():
	g.map_ax.clear()
	mat = g.map_ax.matshow(g.grid, cmap=g.cmap, vmin=0, vmax=3)
	g.map_ax.set_xticks(np.arange(-.5, g.grid.shape[1], 1), minor=True)
	g.map_ax.set_yticks(np.arange(-.5, g.grid.shape[0], 1), minor=True)
	g.map_ax.grid(which='minor', color='w', linestyle='-', linewidth=2)
	g.map_ax.set_xticklabels([])
	g.map_ax.set_yticklabels([])
	g.map_fig.canvas.draw()
	return mat

def plot():
	g.map_fig, g.map_ax = plt.subplots(figsize=(5, 4))
	g.canvas = FigureCanvasTkAgg(g.map_fig, master=g.map_root)  # Embedding figure in Tkinter
	g.canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
	g.map_root.grid_rowconfigure(0, weight=1)
	g.map_root.grid_columnconfigure(0, weight=1)
	mat = plot_grid()

def resize_button():
	resize_button = tk.Button(g.map_root, text="New Grid Size", command=gen_map.ask_for_size)
	resize_button.grid(row=1, column=0, sticky="ew")
	return (resize_button)

def zero_grid(x_size, y_size):	
	return np.zeros((y_size, x_size), dtype=int)

def on_press(event):
	if event.button in [1, 3]:  # Left or right button
		g.mouse_pressed = True
		g.button_used = event.button
		try:
			gen_map.clicked_cell(event.button, (int(np.rint(event.xdata)), int(np.rint(event.ydata))))
		except TypeError:
			pass

def on_release(event):
	g.mouse_pressed = False
	g.button_used = None

def on_motion(event):
	if g.mouse_pressed and g.button_used:
		try:
			ix, iy = int(np.rint(event.xdata)), int(np.rint(event.ydata))
			if 0 <= ix < g.grid.shape[1] and 0 <= iy < g.grid.shape[0]:
				gen_map.clicked_cell(g.button_used, (ix, iy))
		except TypeError:
			pass

def key_hooks():
	g.map_fig.canvas.mpl_connect('button_press_event', on_press)
	g.map_fig.canvas.mpl_connect('button_release_event', on_release)
	g.map_fig.canvas.mpl_connect('motion_notify_event', on_motion)

def exit_ways():
	finished_button = tk.Button(g.map_root, text="Finished", bg="green", command=g.map_root.destroy)
	finished_button.grid(row=2, column=0, sticky="ew")
	key_hooks()
	g.map_root.protocol("WM_DELETE_WINDOW", lambda: [g.map_root.destroy()])
	return finished_button

def instructions():
	instructions = tk.Label(g.map_root, text="Connected green cells will be flooded")
	instructions.grid(row=3, column=0, sticky="ew", padx=10, pady=1)
	instructions = tk.Label(g.map_root, text="Left click/drag red cells to turn them red")
	instructions.grid(row=4, column=0, sticky="ew", padx=10, pady=1)
	instructions = tk.Label(g.map_root, text="Right click/drag green cells to turn them red")
	instructions.grid(row=5, column=0, sticky="ew", padx=10, pady=1)
	instructions = tk.Label(g.map_root, text="Left click/drag a green cell to select it as the starting position or")
	instructions.grid(row=6, column=0, sticky="ew", padx=10, pady=1)
	instructions = tk.Label(g.map_root, text="Right click/drag a red cell to select it as the starting position")
	instructions.grid(row=7, column=0, sticky="ew", padx=10, pady=1)
	instructions = tk.Label(g.map_root, text="Begin is yellow/pink (to fill / not to fill)")
	instructions.grid(row=8, column=0, sticky="ew", padx=10, pady=1)
