import open3d as o3d
PATH = "./data/0000000000.pcd"
pcds = [o3d.io.read_point_cloud(PATH)]
# print how many points there are
print(pcds)

# Visualise the PCD file
o3d.visualization.draw_geometries(pcds)
