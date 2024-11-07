import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np
import cartopy.io.img_tiles as cimgt
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches
from matplotlib import gridspec
import random

"""Reads a neighborhood data file and returns a dictionary containing neighborhood names and coordinates."""


def read_natural_neighborhood(inputfile):
    neighbourhoods = {}
    name = None
    with open(inputfile, "r") as file:
        lines = file.readlines()
        processed_lines = []  # List to store processed line data(Data in the same format)

        for line in lines:
            line = line.strip()  # Remove leading and trailing whitespace
            # Skip comment lines or empty lines
            if line.startswith("#") or not line:
                continue
            # Handle lines containing multiple coordinates in a single line, formatting them to one coordinate per line
            if line.startswith("["):
                line = line[1:-1]  # Remove square brackets at the beginning and end
                values = [float(num) for num in line.replace("(", "").replace(")", "").split(
                    ",")]  # Convert each coordinate string to a list of floating-point numbers
                coordinate = np.array(values).reshape(-1,
                                                      2)  # Reshape coordinates to a 2D array, with one coordinate per row
                for x, y in coordinate:
                    processed_lines.append(f"({x}, {y})")
            else:
                # If not a multi-coordinate line, add it directly to the processed_lines list
                processed_lines.append(line)

        # Organize all processed lines into a dictionary
        for line in processed_lines:
            # Identifying neighbourhood names by the beginning
            if not line.startswith("("):
                name = line
                neighbourhoods[name] = []  # Create an empty list for the new neighborhood
            else:
                # Add the coordinates in the coordinate row to the corresponding neighbourhood list
                elements = line.replace("(", "").replace(")", "").split(",")
                x = float(elements[0])
                y = float(elements[1])
                neighbourhoods[name].append((x, y))
        return neighbourhoods


"""Generates a list of unique colors for differentiating neighborhood areas in a plot."""


def legend_unique_colors(num_colors):
    colors = []

    # Loop to generate colors based on the number of neighborhoods
    for _ in range(num_colors):
        # Generate a random RGB color, with each value between 0 and 255.
        color = (int(random.random() * 255), int(random.random() * 255), int(random.random() * 255))
        # Check if it is a unique colour, if not randomly generate again until unique
        # Divide each colour component by 255, as matplotlib needs to accept colour inputs in the range 0-1
        if (color[0] / 255, color[1] / 255, color[2] / 255) not in colors:
            colors.append((color[0] / 255, color[1] / 255, color[2] / 255))
            # Reach quantity, jump out of loop
            if len(colors) == num_colors:
                break
    return colors


"""Plot natural neighborhoods on a map of Edinburgh with unique colors for each area."""


def plot_natural_neighbourhoods(neighbourhoods):
    # Create figure and set up a two-column layout: map on the left and legend on the right
    fig = plt.figure(figsize=(10, 7))
    gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1])  # Left 3/4 map, right 1/4 legend

    # Set up the map axis with Edinburgh’s projection (OSGB 1936) and extent
    ax = fig.add_subplot(gs[0], projection=ccrs.OSGB(1936))
    ax.set_extent((305000, 339000, 653000, 686000), crs=ccrs.OSGB(1936))

    # Add OpenStreetMap tiles as the background
    osm_tiles = cimgt.OSM()
    ax.add_image(osm_tiles, 11)

    # Generate unique colors for each neighborhood and prepare legend entries
    num_neighbourhoods = len(neighbourhoods)
    colors = legend_unique_colors(num_neighbourhoods)
    patches = []

    # Plot each neighborhood with a unique color
    for i, (name, coordinate) in enumerate(neighbourhoods.items()):
        coordinate = np.array(coordinate)
        x, y = coordinate[:, 0], coordinate[:, 1]
        color = colors[i]
        ax.fill(x, y, color=color, edgecolor="black", transform=ccrs.OSGB(1936), alpha=0.5)
        patches.append(mpatches.Patch(color=color, label=name))

    # Create legend axis and set up the position of legend(bbox_to_anchor,bbox_transform--Anchor the map box to move accordingly)
    legend_ax = fig.add_subplot(gs[1])
    legend_ax.axis("off")
    legend = legend_ax.legend(handles=patches, loc="upper left", fontsize=3.5, frameon=True, ncol=2,
                              handlelength=1, bbox_to_anchor=(1.05, 1.01), bbox_transform=ax.transAxes)
    legend.set_title("Map Legend: Neighborhoods", prop={'size': 6, 'weight': 'bold'})
    legend.get_frame().set_linewidth(0.5)

    # Setting the map title
    fig.suptitle("Edinburgh Natural Neighbourhoods", fontsize=16, fontweight='bold', y=0.95)

    # Add gridlines with latitude and longitude labels for reference
    gridlines = ax.gridlines(draw_labels=True, color='gray', linestyle='--', linewidth=0.4)
    gridlines.top_labels = False
    gridlines.right_labels = False
    gridlines.left_labels = True
    gridlines.bottom_labels = True
    # Set the font size of latitude and longitude labels
    gridlines.xlabel_style = {'size': 8}  # 设置经度标签字体大小
    gridlines.ylabel_style = {'size': 8}  # 设置纬度标签字体大小

    # Adjust the layout to ensure proper spacing between map, legend, and title
    plt.subplots_adjust(left=0.05, right=0.85, top=0.9, bottom=0.1, wspace=0.3)

    # Display the plot
    plt.show()


if __name__ == '__main__':
    data = read_natural_neighborhood('data/natural_neighbourhoods.dat')
    num_colors = len(data)
    plot_natural_neighbourhoods(data)