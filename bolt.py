from dataclasses import dataclass
from stl import mesh
import numpy as np

@dataclass
class Bolt:
    diameter: float
    length: float
    thread_pitch: float
    head_diameter: float
    head_height: float
    torx_size: float

def create_bolt_model(bolt: Bolt) -> mesh.Mesh:
    # Create the 3D model of the bolt using the Bolt class properties
    # In this example, a bolt is modeled simply as a cylinder
    n_points = 100
    theta = np.linspace(0, 2.*np.pi, n_points)
    v = np.zeros((n_points * 2, 3))  # Array for vertices
    
    # Bottom circle vertices
    v[:n_points, 0] = bolt.diameter / 2 * np.cos(theta)
    v[:n_points, 1] = bolt.diameter / 2 * np.sin(theta)
    v[:n_points, 2] = 0

    # Top circle vertices
    v[n_points:, 0] = bolt.diameter / 2 * np.cos(theta)
    v[n_points:, 1] = bolt.diameter / 2 * np.sin(theta)
    v[n_points:, 2] = bolt.length

    f = []  # List for faces
    for i in range(n_points-1):
        # Two triangles for each sector
        f.append([i, (i+1) % n_points, i + n_points])
        f.append([(i+1) % n_points, (i+1) % n_points + n_points, i + n_points])
        
    # Create the mesh
    bolt_mesh = mesh.Mesh(np.zeros(len(f), dtype=mesh.Mesh.dtype))
    for i, face in enumerate(f):
        for j in range(3):
            bolt_mesh.vectors[i][j] = v[face[j], :]
    
    return bolt_mesh

def save_to_stl(bolt_model: mesh.Mesh, file_name: str) -> None:
    # Save the 3D model to an STL file
    bolt_model.save(file_name)

if __name__ == "__main__":
    bolt = Bolt(diameter=8, length=25, thread_pitch=1.25, head_diameter=10, head_height=5, torx_size=25)
    bolt_model = create_bolt_model(bolt)
    save_to_stl(bolt_model, "bolt.stl")
