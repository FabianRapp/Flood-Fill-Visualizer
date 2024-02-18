import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, TextBox
import matplotlib.patches as mpatches
import warnings
import globals as g
import main as m
import main_utils as u

color_dict_labels = {
	"Out of bounds" : 'gray',
	"Do not fill" : 'red',
	"Fill connected zone" : 'green',
	"Currently checking" : 'yellow',
	"Filled: Checked no directions" : 'lightblue',
	"Filled: Checked one direction" : 'skyblue',
	"Filled: Checked two directions" : 'dodgerblue',
	"Filled: Check three direcetions" : 'royalblue',
	"Filled: Checked all directions" : 'navy',
}

def display_area(size):
	plt.ion()
	fig, ax = plt.subplots(figsize=(7, 7))
	ax.axis('off')
	fig.canvas.mpl_connect('close_event', u.on_close)
	return fig, ax

def pause_box():
	text_pos = plt.axes([0.87, 0.092, 0.13, 0.05])
	g.pause_box = TextBox(text_pos, '', initial=f'{((np.log10(g.pause_time) - g.min_val) / (g.max_val - g.min_val)) * 100:.0f}%')
	g.pause_box.set_active(False)
	text_pos.spines['top'].set_visible(False)
	text_pos.spines['right'].set_visible(False)
	text_pos.spines['bottom'].set_visible(False)
	text_pos.spines['left'].set_visible(False)

def speed_slider():
	plt.subplots_adjust(bottom=0.35)
	slider_ax = plt.axes([0.21, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
	g.min_val, g.max_val = np.log10(0.0001), np.log10(4)
	speed_slider = Slider(slider_ax, 'Step time', g.min_val, g.max_val, valinit=np.log10(g.pause_time))
	speed_slider.on_changed(u.update_pause_time)
	pause_box()
	return speed_slider

# warning for potential unsupported figure for tight_layout gets silenced
def legend(fig):
	legend_ax = fig.add_subplot(1, 2, 1)
	legend_ax.axis('off')
	legend_patches = [mpatches.Patch(color=color, label=f"{label}: {color}") for label, color in color_dict_labels.items()]
	legend_ax.legend(handles=legend_patches, loc='upper left', ncol=2, borderaxespad=0.)
	with warnings.catch_warnings():
		warnings.simplefilter("ignore", UserWarning)
		fig.tight_layout()
	return (legend_ax)
