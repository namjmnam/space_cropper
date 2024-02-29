def parse_obj_file(file_path):
    vertices = []  # List of vertices
    faces = []     # List of faces
    lines = []     # List of lines

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if not parts:
                continue  # skip empty lines
            
            if parts[0] == 'v':  # vertex
                # Convert each part to a float and add to the vertices list
                vertices.append([float(part) for part in parts[1:]])
            elif parts[0] == 'f':  # face
                # Convert each part to an integer (assuming no slashes)
                faces.append([int(part.split('/')[0]) for part in parts[1:]])
            elif parts[0] == 'l':  # line
                # Convert each part to an integer
                lines.append([int(part) for part in parts[1:]])
    
    return vertices, faces, lines

# Example usage
file_path = 'path_to_your_obj_file.obj'  # Replace with the path to your .obj file
vertices, faces, lines = parse_obj_file(file_path)
print(vertices)
print(faces)
print(lines)
