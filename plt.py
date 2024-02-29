import tkinter as tk
from tkinter import filedialog
import pandas as pd
import os
from package.index_to_plt import plot_coord
from package.map_to_xlsx import to_xlsx

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

# plot_coord(df, 50, 50, -150, 50)
df_coords = plot_coord(df, 50, 50)
print(df_coords['coord'])

to_xlsx(df, 50, 50)
