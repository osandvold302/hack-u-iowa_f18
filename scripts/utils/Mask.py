#!/usr/bin/env python
# coding: utf-8

# In[11]:


import SimpleITK as sitk


# In[12]:


def gen_mask(subject, eye_segmentation_mask, t1_threshold, t2_threshold):
    brain_mask = sitk.Cast(((subject.seg > 0) * 3), subject.t1.GetPixelIDValue())
    t2_mask = sitk.Cast((subject.t2 > 2000), subject.t1.GetPixelIDValue())
    t1_mask = sitk.Cast((subject.t1 < 1000), subject.t1.GetPixelIDValue())
    eye_segmentation_mask = eye_segmentation_mask * t1_mask * t2_mask
    return closure_function(eye_segmentation_mask, 8)# + closure_function(brain_mask, 5)


# In[13]:


def closure_function(mask, mag):
    dilated = sitk.BinaryDilate(mask, mag)
    return sitk.BinaryErode(dilated, mag)


# In[ ]:


path = '/Volumes/easystore/PHD_NIFTI_NET_CONFIG/images/'
