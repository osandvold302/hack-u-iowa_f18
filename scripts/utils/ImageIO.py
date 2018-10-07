#!/usr/bin/env python
# coding: utf-8

# In[22]:


import SimpleITK as sitk
import os
import glob
import pandas as pd


# In[23]:


class Subject(object):
    def __init__(self, identifier, t1, t2, seg, fcsv):
        fcsv[1] = -fcsv[1]
        fcsv[2] = -fcsv[2]
        self.identifier = identifier
        self.t1 = t1 # sitk.Image()
        self.t2 = t2 # sitk.Image()
        self.seg = seg # sitk.Image()
        self.RE = fcsv.loc[fcsv[0] == 'RE'].values[0][1:4] # physical point 3-tuple of right eye
        self.LE = fcsv.loc[fcsv[0] == 'LE'].values[0][1:4] # physical point 3-tuple of left eye


# In[24]:


def get_subject_list(directory:str, glob_regex):
    subjects = set()
    for file in glob.glob(directory+'/'+glob_regex):
        path = os.path.join(directory, file)
        if os.path.isfile(path):
            subjects.add(file.replace('_t1w.nii.gz',''))
    return list(subjects)


# In[25]:


def get_subject(identifier:str, directory:str):
    reader = sitk.ImageFileReader()
    reader.SetFileName(os.path.join(directory, '{identifier}_t1w.nii.gz'.format(identifier=identifier)))
    t1=reader.Execute()
    reader.SetFileName(os.path.join(directory, '{identifier}_t2w.nii.gz'.format(identifier=identifier)))
    t2=reader.Execute()
    reader.SetFileName(os.path.join(directory, '{identifier}_seg.nii.gz'.format(identifier=identifier)))
    seg=reader.Execute()
    fcsv=pd.read_csv(os.path.join(directory, '{identifier}.fcsv'.format(identifier=identifier)), comment='#', header=None)
    return Subject(identifier=identifier, t1=t1,t2=t2,seg=seg,fcsv=fcsv)  

