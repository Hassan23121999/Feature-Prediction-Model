import open3d as o3d
import numpy as np
import tkinter as tk
from tkinter import filedialog
import os

def stl_to_point_cloud(stl_file_path, number_of_points=2048):
    # Convert an STL file to a point cloud
    mesh = o3d.io.read_triangle_mesh(stl_file_path)

    if not mesh.is_watertight():
        print(f"Mesh {stl_file_path} is not watertight, attempting to repair")
        mesh = mesh.remove_duplicated_triangles()
        mesh = mesh.remove_duplicated_vertices()
        mesh = mesh.remove_degenerate_triangles()

    point_cloud = mesh.sample_points_poisson_disk(number_of_points)
    points = np.asarray(point_cloud.points)
    return points

def save_point_cloud_to_txt(point_cloud, output_path):
    # Save the point cloud to a text file
    np.savetxt(output_path, point_cloud, fmt='%f')

def process_folder(folder_path):
    # Process all STL files in the given folder
    for file in os.listdir(folder_path):
        if file.lower().endswith('.stl'):
            stl_file_path = os.path.join(folder_path, file)
            output_path = os.path.join(folder_path, os.path.splitext(file)[0] + '.txt')

            point_cloud = stl_to_point_cloud(stl_file_path)
            save_point_cloud_to_txt(point_cloud, output_path)
            print(f"Processed {file} - Point cloud saved to {output_path}")

def main():
    # Create a GUI for folder selection
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Ask the user to select a folder
    folder_path = filedialog.askdirectory(title='Select Folder Containing STL Files')
    if not folder_path:
        return

    # Process all STL files in the folder
    process_folder(folder_path)

    print("All STL files in the folder have been processed.")

if __name__ == "__main__":
    main()
