import transforms3d
import numpy as np

def mocap2smpl(data, m, global_rotation=[0,0,0.00001]):
    ### global transform
    p = data[89,90,91] # Pelvis
    p_eulr = transforms3d.euler.axangle2euler(p/np.linalg.norm(p), np.linalg.norm(p)/180*np.pi, 'sxyz')
    p_transform_woz = transforms3d.euler.euler2mat(p_eulr[0], p_eulr[1], 0)
    p_transform = transforms3d.axangles.axangle2mat(p/np.linalg.norm(p), np.linalg.norm(p)/180*np.pi)
    global_transform = transforms3d.axangles.axangle2mat(global_rotation, np.linalg.norm(global_rotation))
    body_rotation = transforms3d.axangles.mat2axangle(np.dot(global_transform, p_transform_woz))
    m.pose[0:3] = body_rotation[0][[1, 2, 0]]*body_rotation[1]

    ### Left_UpperLeg transform
    lfe = data[17:20] # LFemur
    lfe_transform = transforms3d.axangles.axangle2mat(lfe/np.linalg.norm(lfe), np.linalg.norm(lfe)/180*np.pi)
    lhip_transform = np.dot(np.linalg.inv(p_transform), lfe_transform) # relative rotation
    lhip = transforms3d.axangles.mat2axangle(lhip_transform)
    m.pose[3:6] = lhip[0][[1, 2, 0]]*lhip[1]

    ### Right_UpperLeg transform
    rfe = data[113:116] # RFemur
    rfe_transform = transforms3d.axangles.axangle2mat(rfe/np.linalg.norm(rfe), np.linalg.norm(rfe)/180*np.pi)
    rhip_transform = np.dot(np.linalg.inv(p_transform), rfe_transform)
    rhip = transforms3d.axangles.mat2axangle(rhip_transform)
    m.pose[6:9] = rhip[0][[1, 2, 0]]*rhip[1]

    ### Left_LowerLeg transform
    lti = data[71:74] # LTibia
    lti_transform = transforms3d.axangles.axangle2mat(lti/np.linalg.norm(lti), np.linalg.norm(lti)/180*np.pi)
    lk_transform = np.dot(np.linalg.inv(lfe_transform), lti_transform)
    lk = transforms3d.axangles.mat2axangle(lk_transform)
    m.pose[12:15] = lk[0][[1, 2, 0]]*lk[1]

    ### Right_LowerLeg transform
    rti = data[167:170] # RTibia
    rti_transform = transforms3d.axangles.axangle2mat(rti/np.linalg.norm(rti), np.linalg.norm(rti)/180*np.pi)
    rk_transform = np.dot(np.linalg.inv(rfe_transform), rti_transform)
    rk = transforms3d.axangles.mat2axangle(rk_transform)
    m.pose[15:18] = rk[0][[1, 2, 0]]*rk[1]

    ### Left_Foot (90 offset)
    lfo = data[26:29]
    lfo_transform = transforms3d.axangles.axangle2mat(lfo/np.linalg.norm(lfo), np.linalg.norm(lfo)/180*np.pi)
    lfo_transform = np.dot(lfo_transform, transforms3d.axangles.axangle2mat([0,1,0], np.pi/2))
    la_transform = np.dot(np.linalg.inv(lti_transform), lfo_transform)
    la = transforms3d.axangles.mat2axangle(la_transform)
    m.pose[21:24] = la[0][[1, 2, 0]]*la[1]

    ### Right_Foot (90 offset)
    rfo = data[122:125]
    rfo_transform = transforms3d.axangles.axangle2mat(rfo/np.linalg.norm(lfo), np.linalg.norm(rfo)/180*np.pi)
    rfo_transform = np.dot(rfo_transform, transforms3d.axangles.axangle2mat([0,1,0], np.pi/2))
    ra_transform = np.dot(np.linalg.inv(rti_transform), rfo_transform)
    ra = transforms3d.axangles.mat2axangle(ra_transform)
    m.pose[24:27] = ra[0][[1, 2, 0]]*ra[1]

    ###

