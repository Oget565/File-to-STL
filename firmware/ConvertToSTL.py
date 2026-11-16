from stl import mesh
import numpy as np

class ConvertToSTL:
    def __init__(self, file, buildplate):
        self.file = file
        self.width, self.lenght = buildplate

    def verifytest(self): #delete later
        return f"dimensions: {self.width}, {self.lenght}"

    def converttostl(self):
        numbers = np.fromfile(self.file, dtype=np.uint8)
        n = numbers.size

        vertices = np.array([
        [-1, -1, -1], [+1, -1, -1], [+1, +1, -1], [-1, +1, -1],
        [-1, -1, +1], [+1, -1, +1], [+1, +1, +1], [-1, +1, +1],
        ])
        faces = np.array([
            [0, 3, 1], [1, 3, 2], [0, 4, 7], [0, 7, 3],
            [4, 5, 6], [4, 6, 7], [5, 1, 2], [5, 2, 6],
            [2, 3, 6], [3, 7, 6], [0, 1, 5], [0, 5, 4],
        ])
        cube_template = (vertices + 1) / 2

        cell = 5
        side = int(np.ceil(np.sqrt(n)))

        area = self.width * self.lenght
        cube_area = cell * cell
        used_area = 0

        grid = [1] * int(area / cube_area)
        cols = int(self.width // cell)
        cubes = []

        level = 0
        new_level = 0

        for number in numbers:
            if used_area >= area:
                new_level = new_level + level + 1
                level = 0
                used_area = 0
                grid = [1] * int(area / cube_area)

            slot = grid.index(1)
            cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))

            x = (slot % cols) * cell
            y = (slot // cols) * cell
            h = cell + number / 255 * 20
            
            placed = cube_template * [cell, cell, h] + [x, y, new_level]

            for i, f in enumerate(faces):
                for j in range(3):
                    cube.vectors[i][j] = placed[f[j], :]

            cubes.append(cube)
            grid[slot] = 0
            used_area += cube_area

            if level < h:
                level = h
            
        result = mesh.Mesh(np.concatenate([c.data for c in cubes]))
        result.save("output.stl")
                

