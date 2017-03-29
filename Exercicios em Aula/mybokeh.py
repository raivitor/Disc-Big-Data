#write/save cell contents into mybokeh.py (use -a to append). 

# Import the ColumnDataSource, figure class from bokeh.plotting
from bokeh.plotting import ColumnDataSource, figure

# Import the widgets
from bokeh.layouts import widgetbox, column
from bokeh.models import Slider

# Import numpy
import numpy as np

# Import current document
from bokeh.io import curdoc#write/save cell contents into mybokeh.py (use -a to append). 


# Define a callback function: callback
def callback(attr, old, new):

    # Read the current value of the slider: scale
    scale = slider.value

    # Compute the updated y using np.cos(scale/x): new_y
    new_y = np.sin(scale/x)
    
    # Update source with the new data values
    source.data = {'x': x, 'y': new_y}    
# Dataset
x = np.arange(0,10,0.1)
y = np.sin(x)

# Create ColumnDataSource: source
source = ColumnDataSource(data={'x': x, 'y': y})

# Create a figure
p = figure(x_axis_label='x values', y_axis_label='Sin(x)')

# Add a line to the plot
p.line('x', 'y', source=source)

# Create first slider: slider1
slider = Slider(title='slider1', start=0, end=10, step=0.1, value=2)
# Attach the callback to the 'value' property of slider
slider.on_change('value',callback)

# Create layout and add to current document
layout = column(widgetbox(slider), p)
curdoc().add_root(layout)