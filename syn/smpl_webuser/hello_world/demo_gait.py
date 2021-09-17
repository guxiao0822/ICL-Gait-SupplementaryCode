'''
Modified from hellp_smpl.py with mocap2smpl function added
'''

from smpl_webuser.serialization import load_model
import numpy as np
from smpl_webuser.utils import mocap2smpl

## Load SMPL model (here we load the female model)
## Make sure path is correct
m = load_model( '../../models/basicmodel_m_lbs_10_207_0_v1.1.0.pkl' )

## Assign random pose and shape parameters
# m.pose[:] = np.random.rand(m.pose.size) * .2
m.betas[:] = np.random.rand(m.betas.size) * .03

## assign poses from ICL
import scipy.io as sio
data = sio.loadmat('../../models/pose.mat')['pose'][0]
mocap2smpl(data, m)

## Write to an .obj file
outmesh_path = './gait_smpl.obj'
with open( outmesh_path, 'w') as fp:
    for v in m.r:
        fp.write( 'v %f %f %f\n' % ( v[0], v[1], v[2]) )

    for f in m.f+1: # Faces are 1-based, not 0-based in obj files
        fp.write( 'f %d %d %d\n' %  (f[0], f[1], f[2]) )

## Print message
print '..Output mesh saved to: ', outmesh_path
