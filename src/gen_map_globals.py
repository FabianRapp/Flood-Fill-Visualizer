import numpy as np
import matplotlib.colors as colors

x_size = 8
y_size = 5
begin = (0, 0)
zone = [
	"11111111",
	"10001001",
	"10010001",
	"10110001",
	"11100001",
]
grid = np.array([[int(cell) for cell in row] for row in zone], dtype=int)

color_dict = {
	0 : 'red',
	1 : 'green',
	2 : 'pink',
	3 : 'yellow',
}
cmap = colors.ListedColormap([color_dict[i] for i in color_dict])

mouse_pressed = False
button_used = None

global canvas, map_ax, map_fig, map_root
