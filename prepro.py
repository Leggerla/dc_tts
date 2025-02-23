# -*- coding: utf-8 -*-
#/usr/bin/python2
'''
By kyubyong park. kbpark.linguist@gmail.com.
https://www.github.com/kyubyong/dc_tts
'''

from __future__ import print_function

from utils import load_spectrograms
import os
from data_load import load_data
import numpy as np
import tqdm
from hyperparams import Hyperparams as hp

# Load data
fpaths, _, _ = load_data() # list

for fpath in tqdm.tqdm(fpaths):
    fname, mel, mag = load_spectrograms(fpath)
    
    #os.mkdir(hp.data+"mels", exist_ok=True)
    #os.mkdir(hp.data+"mags", exist_ok=True)
        
    num = int(fname.split('-')[-1].split('.')[0])
    folder_num = num // 1000
    subfolder_num = (num % 1000) // 100
    
    #os.mkdir(hp.data+"mels/"+str(folder_num), exist_ok=True)
    #os.mkdir(hp.data+"mags/"+str(folder_num), exist_ok=True)

    os.makedirs(hp.data+"mels/"+str(folder_num)+"/"+str(subfolder_num), exist_ok=True)
    os.makedirs(hp.data+"mags/"+str(folder_num)+"/"+str(subfolder_num), exist_ok=True)
    
    np.save(hp.data+"mels/"+str(folder_num)+"/"+str(subfolder_num)+"/"+"{}".format(fname.replace(".wav", ".npy")), mel)
    np.save(hp.data+"mags/"+str(folder_num)+"/"+str(subfolder_num)+"/"+"{}".format(fname.replace(".wav", ".npy")), mag)
