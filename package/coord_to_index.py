import pandas as pd
import numpy as np

def to_index(data, scale, minX=None, maxX=None, minY=None, maxY=None, minZ=None, maxZ=None):
    # Reading the data
    data = data.reset_index(drop=True)
    X = data.iloc[:, 0].values
    Y = data.iloc[:, 1].values
    Z = data.iloc[:, 2].values

    # Calculating the number of cells in each direction
    # Here, max and min needs to be the boundaries of the frame, not actually max and min of each
    if minX==None: minX = np.min(X)
    if minY==None: minY = np.min(Y)
    if minZ==None: minZ = np.min(Z)
    if maxX==None: maxX = np.max(X)
    if maxY==None: maxY = np.max(Y)
    if maxZ==None: maxZ = np.max(Z)
    nx = int(round(scale * (maxX - minX))) + 1  # Ensure nx is an integer
    ny = int(round(scale * (maxY - minY))) + 1  # Ensure ny is an integer
    nz = int(round(scale * (maxZ - minZ))) + 1  # Ensure nz is an integer

    def coord_to_index(x, y, z):
        ix = (x - minX) * scale + 1
        iy = (y - minY) * scale + 1
        iz = (maxZ - z) * scale + 1  # 역순으로 변경
        i = (iz-1) * (nx * ny) + (iy-1) * nx + (ix-1) + 1
        return round(i)

    # 좌표 인덱스화
    data['I'] = data.apply(lambda row: coord_to_index(row['x'], row['y'], row['z']), axis=1)
    data['P'] = 1
    data = data[['I', 'P']]
    data = data.sort_values(by='I', ascending=True, ignore_index=True)

    df = pd.DataFrame({'I': range(1, nx*ny*nz+1)})
    merged_df = pd.merge(data, df, on='I', how='outer')
    merged_df = merged_df.fillna(0)
    merged_df['P'] = merged_df['P'].astype(int)
    merged_df = merged_df.sort_values(by='I', ascending=True, ignore_index=True)
    merged_df = merged_df.drop_duplicates(keep="first")
    print(merged_df)

    print("Grid size (x, y, z, xyz) :", nx, ny, nz, nx*ny*nz)
    print("Make sure to delete column title row")

    return merged_df, nx, ny, nz