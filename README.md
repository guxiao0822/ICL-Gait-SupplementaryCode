# ICL-Gait Dataset 1.0 
Release Date: Sept 2021 

## Primary Contact
**Xiao Gu**, xiao.gu17@imperial.ac.uk Imperial College London

**Yao Guo**, yao.guo@sjtu.edu.cn Shanghai Jiao Tong University

## Citing
Please cite the following paper for the use of this dataset

Gu, Xiao, et al. "Occlusion-Invariant Rotation-Equivariant Semi-Supervised Depth Based Cross-View Gait Pose Estimation." arXiv preprint arXiv:2109.01397 (2021).

## Supplementary Code
* `vis_demo` provides script to visualize the data from different modalities
* `syn` provides script to generate synthetic data based on SMPL

## Dataset Details
The dataset contains a real-world gait dataset collected from multiple viewpoints.
Please see our [paper](https://arxiv.org/pdf/2109.01397) and the [website](https://xiaogu.site/ICL_gait) for more details. 

## Data-Split Experiment Settings
Please follow the settings in our [paper](https://arxiv.org/pdf/2109.01397) to benchmark your algorithms.

### Cross-Subject (CS) Validation (2 loops)
For cross-subject validation, the data were split to two groups {S01, S02, S04, S07}, {S03, S05, S06, S8}. 

Each loop, use one group as training, and the other group as testing set. 

### Cross-View (CV) Validation (5 loops)
For cross-view validation, the data were split based on the five views. 

Each loop, use the data from one view as training, the data from the other views as testing.  
### Cross-Subject Cross-View (CS-CV) Validation (10 loops)
For cross-subject & cross-view validation, the data was split to ten subgroups as a combination of CS and CV validation. 

For example, one group is {S01-V01, S02-V01, S04-V01, S07-V01}. In each loop, use one group as the training set, and report the results on the remaining nine groups.

**You can further split some proportion from the training set as a validation set, but any use of the testing data during training is not allowed.**


## Folder Details
### Dataset folder format
S##_V##_C## refers to the data of the trial per subject, condition, and viewpoint. 
S##: subject id
V##: viewpoint 
C##: walking condition

Each folder contains 300 consecutive samples from one trial (the remaining samples leading to a much large data volume will be released in the future). 
Missing trials (S1-C1-V1, S1-C2-V2, S1-C4-V1, S3-C3-V3, S5-C4-V4, S8-C2-V3, S8-C2-V4, S8-C4-V3, S8-C5-V3)

* **depth**: contains the depth images recorded by RealSense D435
  
  ```
  scale = 0.0010000000474974513;
  fx = 928.108;  fy = 927.443;
  cx = 647.394;  cy = 361.699
  ```
* **mask**:  contains the segmentation mask predicted from RGB images (access suspended) by CDCL
  ```
  ROI (lower-limb) RGB Value [255,127,127; 0,127,255; 0,0,255; 255,255,127; 127,255,127; 0,255,0]
  ```
* **point cloud**:  contains the point cloud converted from depth data, corresponding 3D keypoint, and root orientation
  
* **pose_2d**:  contains the 2D keypoints predicted by OpenPose

* **kinematics**: contains the kinematics (randomly picked, not synchronized with the modalities above) which can be used synthetic data generation




