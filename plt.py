import tkinter as tk
from tkinter import filedialog
import pandas as pd
import os
from package.index_to_plt import plot_coord
from package.map_to_xlsx import to_xlsx
from package.coord_to_index import to_index

# Get the script directory
script_directory = os.path.dirname(os.path.abspath(__file__))

def load_csv():
    # Open a dialog to choose the CSV file
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")], initialdir=script_directory+'/input')
    if file_path:  # If a file was selected
        # Load the CSV file into a pandas DataFrame
        df = pd.read_csv(file_path, header=None)
        return df

df = load_csv()
df.columns = ['I', 'P']

size_x = 50
size_y = 50

# plot_coord(df, 50, 50, -150, 50)
df_coords = plot_coord(df, size_x, size_y)

# Cropping all zero's
df_coords[['x', 'y', 'z']] = pd.DataFrame(df_coords['coord'].tolist(), index=df_coords.index)
df_cropped = df_coords[['x', 'y', 'z']]

df_cropped = df_cropped.drop_duplicates()
df_cropped = df_cropped.reset_index(drop=True)

x_min = df_cropped['x'].min()
y_min = df_cropped['y'].min()
df_cropped['x'] = df_cropped['x'] - x_min
df_cropped['y'] = df_cropped['y'] - y_min

# print(df_cropped)
x_max = df_cropped['x'].max()
x_min = df_cropped['x'].min()
y_max = df_cropped['y'].max()
y_min = df_cropped['y'].min()
z_max = df_cropped['z'].max()
z_min = df_cropped['z'].min()

# Save cropped data
df_for_save, nx, ny, nz = to_index(df_cropped, 1, x_min, x_max, y_min, y_max)
df_cropped.to_csv(script_directory+'/output/'+'cropped_coords.csv', index=False)
df_for_save.to_csv(script_directory+'/output/'+f'cropped_index_{nx}x{ny}x{nz}.csv', index=False)

# print(x_min, x_max, y_min, y_max, z_min, z_max)

# Is the map flat with no floors?
map_is_flat = True
if map_is_flat: df_cropped['z'] = 0

df_re_indexed, nx, ny, nz = to_index(df_cropped, 1, x_min, x_max, y_min, y_max)
# print(df_re_indexed)

# _ = plot_coord(df_re_indexed, x_max+1, y_max+1)

to_xlsx(df_re_indexed, x_max+1, y_max+1)
# Done!


# Uncropped
df_uncropped = df_coords[['x', 'y', 'z']]
if map_is_flat: df_uncropped['z'] = 0
df_uncropped = df_uncropped.drop_duplicates()
df_uncropped = df_uncropped.reset_index(drop=True)
z_max = df_uncropped['z'].max()
z_min = df_uncropped['z'].min()
df_re, nx, ny, nz = to_index(df_uncropped, 1, 0, size_x-1, 0, size_y-1, z_min, z_max)

to_xlsx(df_re, size_x, size_y)
