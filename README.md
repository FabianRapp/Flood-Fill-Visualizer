## Flood-Fill-Visualizer<br>
An educational tool to visualize a recursive function with multiple recursive calls in all directions.
The algorithm checks the current cell, if it is to be filled it fills it and calls the algorithm first on the above cell, when that returns on the below cell, after that recursive call returns on the right cell and finally after the right recursive call returned it calls the algorithm  recursivly on the left cell.

## Dependencies
Python 3.11.7<br>
matplotlib                3.8.4<br>
numpy                     1.26.4<br>
<br>

## How to run
<br>
Install Python: If not already installed install Python 3.11.7 (which I used to run this tool)<br>
try `python --version` or `python3 --version`<br>
`https://www.python.org/downloads/release/python-3117/`<br>
<br>
Download the program:<br>
`git clone https://github.com/FabianRapp/Flood-Fill-Visualizer.git && cd Flood-Fill-Visualizer`<br>
<br>
Set up the enviorment:<br>
`python3 -m venv flood_fill_env && source flood_fill_env/bin/activate && pip install matplotlib==3.8.4 numpy==1.26.4`<br>
<br>
Finally to run the program:<br>
`python main.py`<br>
<br>
To run it again close the windows and use `python main.py`<br>

## The first window: Setup
Configure the grid by changing cells between being walls or empty spaces, and setting the starting position<br>
<br>
![Setup window](images/Flood-Fill-Visualizer-Setup.png)
<br>
Green Cells: Space empty space (Cells that can be filled)<br>
Red Cells: Walls (Cells that can not be filled)<br>
Yellow Cell: Starting position in cell that can be filled<br>
Grey Cell: Starting position in cell that can not be filled<br>

# Controls:
Left click a red cell to turn it green<br>
Right click a green cell to turn it red<br>
Left click a green cell to select it as the starting postion<br>
Right click a red cell to select it as the starting postion (algorithm will fill nothing)<br>
Instead of clicking individual cells the mouse can be dragged over while the mouse button is held to "click" all the cells passed<br>
To change the grid size click "New Grid Size"<br>
<br>
After you have configured the map press "Start"<br>

## The second window: Visualization
This window visualizes the recursive execution of the flood fill algorithm in real-time<br>
![Visualization window](images/Flood-Fill-Visualizer.png)

This is where the main algorithm runs and is displayed.<br>
The algorithm works recursively by calling itself first on the above cells, then the below cell, right cell and finally the left cell (in case the current cell is to be filled).<br>

Move the slider on the bottom the the left for higher speed.<br>

# The colors:
Green: Empty space (can be filled)<br>
Red: Wall (can not be filled)<br>
Yellow: Current postion<br>
All blue gradiants: Filled cells<br>
Grey: Boarders<br>

Darkest blue: the cell is filled and has already called the recusricve call on all it's adjacent cells and all have already returned.<br>
Lightest blue: the cell is filled and has called one (the above cell)<br>
Inbetween blue: Filled cell that has called the algorithm on more adjacent cells the darker the blue is<br>
