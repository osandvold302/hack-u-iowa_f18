#!/usr/bin/env python
# coding: utf-8

# In[1]:


import SimpleITK as sitk


# In[7]:


def create_spherical_mask(subject):
    # Get the voxel from the physical space point
    LE_voxel = subject.t1.TransformPhysicalPointToIndex(subject.LE)
    RE_voxel = subject.t1.TransformPhysicalPointToIndex(subject.RE)
    
    # Eye diameter across vertically approx 18-19 mm
    # Eye diameter across horizontally approx 20 mm
    mask = subject.t1*0   # Create mask of image size
    mask[LE_voxel] = 1    # Set center of eye to 1
    dilated_image_LE = sitk.BinaryDilate(mask, 10)  # Create 'sphere' for eye, r=10
    mask = subject.t1*0   # Repeat
    mask[RE_voxel] = 1
    dilated_image_RE = sitk.BinaryDilate(mask, 10) # binary image
    mask_LE_RE = (dilated_image_LE, dilated_image_RE)

    return mask_LE_RE


# In[1]:


def get_thresholds(subject):
    # Get the threshold by multiplying the image by left and right eye masks
    mask_LE_RE = create_spherical_mask(subject)
    stat_filter = sitk.StatisticsImageFilter()
    stat_filter.Execute(subject.t1*mask_LE_RE[0] + subject.t1*mask_LE_RE[1])
    T1_threshold = stat_filter.GetMean()
    stat_filter.Execute(subject.t2*mask_LE_RE[0] + subject.t2*mask_LE_RE[1])
    T2_threshold = stat_filter.GetMean()
    return (T1_threshold, T2_threshold)


# In[2]:


# Uses a spherical shape to create left eye and right eye masks w/ scaling
# 1 times LE and 2 times RE
def getTotalMask(subject):
    mask_LE_RE = create_spherical_mask(subject)
    return mask_LE_RE[0]*1 + mask_LE_RE[1]*2


# In[ ]:




