% this is the script used for visualizing samples from ICL-Gait Dataset
% https://xiaogu.site/ICL_gait/
% Contact: xiao.gu17@imperial.ac.uk 

clear all;
close all;
clc;

figure();
%% visualize depth
depth = imread('depth.png');
subplot(2,2,1);
imshow(depth);
colormap('parula');
caxis([0,3000]);
title('depth image');

%% visualize mask
mask = imread('mask.png');
subplot(2,2,2);
imshow(mask);
title('segmentation mask');

%% visualize skeleton from openpose
% load openpose result
fid = fopen('keypoint.json'); 
raw = fread(fid,inf); 
str = char(raw'); 
fclose(fid); 
val = jsondecode(str);
pose2d = reshape(val.people.pose_keypoints_2d, 3, 25)';

% visualize 2d result
j_index = [9,10,11,12,13,14,15,20,21,22,23,24,25];
j_tree = [9,10;10,11;11,12;12,23;12,25;23,24; 
          9,13;13,14;14,15;15,20;15,22;20,21];
subplot(2,2,3);
plot(pose2d(j_index,1), pose2d(j_index,2),'.','MarkerSize',25);
hold on;

for j = 1:size(j_tree,1)
    plot(pose2d(j_tree(j,:),1), pose2d(j_tree(j,:),2),'-', 'LineWidth', 3);    
end

imshow([]);
xlim([400, 1000]);
ylim([50, 600]);
title('2D Keypoint');

%% visualize point cloud
load('pointcloud.mat');
subplot(2,2,4);
pcshow(pc_2048,'VerticalAxis','Y','VerticalAxisDir','down')
hold on;
pcshow(keypoint,'VerticalAxis','Y','VerticalAxisDir','down', 'MarkerSize', 300)
title('\color{black}Point Cloud');
set(gca, 'color', 'w');
set(gcf, 'color', 'w');
axis off;

% visualize the body_orientation (of pelvis)
plotTransforms((keypoint(1,:)+keypoint(5,:))/2, body_orientation, 'FrameSize',0.2);
