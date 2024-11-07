# Python Programming Assignment

## Data Plotting Project
This project reads data from a file and plots it using `matplotlib`. 

### Features
- **Dynamic Plotting**: Plots the data with `matplotlib`, labeling axes and including a grid.
- **Framework**:Simple structure allows for easy modifications of plot labels, title, and grid style.

### Function Overview
**Function**:This project contains only one function - read_data, which reads data from a specified file and plots it using `matplotlib`.

**Parameters**:inputfile: Path to the input data file.

## Edinburgh Neighborhood Mapping Project
This project visualizes different neighborhoods in Edinburgh by plotting them on a map with unique colors. The visualization includes a legend that labels each neighborhood, allowing for easy identification.

### Features
- **Unique Color Mapping**: Each neighborhood is assigned a unique color for easy differentiation.
- **Gridlines**: The map includes labeled gridlines for reference.
- **Map Background**: OpenStreetMap tiles are used as the map background for additional spatial context.

### Function Overview
This section contains three main functions, designed to process neighborhood data, generate unique colors, and plot the data on a map. 
#### 1. `read_natural_neighborhood(inputfile)`
**Function**: Reads a neighborhood data file and returns a dictionary containing neighborhood names and coordinates.

**Parameters**:inputfile: Path to the file containing neighborhood names and coordinates.
#### 2. `legend_unique_colors(num_colors)`
**Function**:Generates a list of unique RGB colors for differentiating neighborhood areas in a plot.

**Parameters**:num_colors: The number of unique colors to generate. This should match the number of neighborhoods or regions to be plotted.
#### 3. `plot_natural_neighbourhoods(neighbourhoods)`
**Function**:Plots the neighborhoods on a map of Edinburgh using unique colors and displays a legend for reference.

**Parameters**:neighbourhoods: Dictionary where keys are neighborhood names and values are lists of (x, y) coordinates.
### Prerequisites

This project requires Python and several libraries. To install dependencies, use the following command:
```bash 
pip install matplotlib
pip insatll numpy
pip install cartopy
pip install scipy