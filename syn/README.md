# ICL-Gait to SMPL

We provide the script [utils.py](smpl_webuser/utils.py) for transferring the gait parameter from our dataset to SMPL

## Usage 
* Please download the repository of [SMPL](smpl_webuser/utils.py) 

* Add `models/pose.mat` to `models` of SMPL respository

* Add `smpl_webuser/hello_world/demo_gait.py` to `smpl_webuser/hello_world/`

* (optional) replace the `smpl_webuser/serialization.py` by a modified `smpl_webuser/serialization.py` compatible with python3

* Running `demo_gait.py`, a synthetic model will be generated automatically





