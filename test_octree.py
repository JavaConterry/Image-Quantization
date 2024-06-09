import open3d as o3d
import numpy as np

# Create some sample points
points = np.random.rand(100, 3)  # 100 random points

# Create a point cloud object
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)

# Create an octree
octree = o3d.geometry.Octree(max_depth=4)
octree.convert_from_point_cloud(pcd, size_expand=0.01)

# Visualize the octree
o3d.visualization.draw_geometries([octree])