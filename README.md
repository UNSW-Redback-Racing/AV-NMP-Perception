# AV-NMP-Perception

## Introduction
The perception team is responsible for how the car perceives its environment and makes sense of it using the information it gets from LIDAR sensors and cameras. This involves pre-processing, cone classification using CNNs, and interfacing those results with SLAM subsystem. The current goal for AV Perception is to setup a LIDAR pipeline (and cameras later on). In this NMP, you'll be working on the pre-processing stage for LIDAR specifically. 

## Task
Your task is to perform run through 3 pre-processing steps as outlined below on the pointcloud dataset given to you in the data folder (in .pcd format). You can implement this in Python, C++, or Rust. We recommend using the Open3D library for Python and PCL library for C++ (we have provided links at the bottom). 


### Filtering
LIDAR data is represented by points (x,y,z) with intensity. A single scan can have upto millions of points, so we need a way to filter out irrelevant data to increase processing speed (while balancing accuracy). This can be done through
- Downsampling: e.g converting points to voxels
- Crop/FOV trimming: Removing points outside limits

### Segmentation
We take the filtered data and divide them into planes and objects. This helps identify the road (plane), and other objects (like cones), which we can later use to perform ground removal. A common way to do this is to use the RANSAC algorithm. 
### Clustering
Clustering puts points together in sets and helps identify different types of objects. A common way to achieve this is to perform Euclidean clustering (usually implemented using a KDTree). The 3D Libraries should have their own apis written for this which uses the DBSCAN algorithm, but you're welcome to implement another clustering algorithm.

![image](https://user-images.githubusercontent.com/29827456/135599351-25c5b187-0db6-46e7-b277-8d6cf6f5bf68.png)

## Submission
Fork this repository, and clone it. Then work through the three stages. We have provided a basic Python script which just visualises a pcd file for you using Open3D. The final submission should contain all your project files and be able to visualise it (you can just visualise them using the libraries). 
## Useful Links

Python: http://www.open3d.org/docs/release/index.html#python-api-index

C++: https://pointclouds.org/documentation/

**Open3D**
- Downsampling, cropping, DBScanning and other stuff: http://www.open3d.org/docs/release/tutorial/geometry/pointcloud.html#Point-cloud

**PCL**
- Downsampling: https://pointclouds.org/documentation/tutorials/voxel_grid.html
- Cropping: https://pointclouds.org/documentation/classpcl_1_1_crop_box_3_01pcl_1_1_p_c_l_point_cloud2_01_4.html
- RANSAC: https://pointclouds.org/documentation/classpcl_1_1_random_sample_consensus.html
- Clustering: https://pcl.readthedocs.io/en/latest/cluster_extraction.html
