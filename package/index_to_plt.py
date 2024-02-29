import matplotlib.pyplot as plt

def index_to_coord(i, max_z, min_x, min_y, nx, ny):
    # Calculate indices ix, iy, iz
    iz = (i - 1) // (nx * ny) + 1
    iy = ((i - 1) % (nx * ny)) // nx + 1
    ix = ((i - 1) % nx) + 1

    # Calculate x, y, z
    x = (ix - 1) + min_x
    y = (iy - 1) + min_y
    z = max_z - (iz - 1)

    return x, y, z

def plot_coord(df, nx, ny, z_min=-300, z_max=300):
    df = df.loc[df.iloc[:, 1] != 0]
    df['coord'] = df['I'].apply(lambda x: index_to_coord(x, 0, 0, 0, nx, ny))
    # print(df)

    # Extracting x, y, z coordinates
    x = df['coord'].apply(lambda t: t[0])
    y = df['coord'].apply(lambda t: t[1])
    z = df['coord'].apply(lambda t: t[2])

    # Creating a 3D scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)

    # Adding labels and title (optional)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_title('3D Scatter Plot')

    ax.set_zlim(z_min, z_max)
    # Showing the plot
    plt.show()
    return df