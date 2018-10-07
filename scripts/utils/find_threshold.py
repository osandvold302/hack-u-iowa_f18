# Write a script to read in T1 and T2 weighted images
# Figure out what threshold to use for the fluid around the eye

# Notes:
# image.transform physical to index
# Take in a dict with all of the image filenames
# Iterate over all the images
# For each image, get RE, LE, transform to voxel
# Find X by X amount of surrounding pixel values
# Average, sum to a total mean
# Report mean and std

# Pass Label Statistics Mask -- 

import SimpleITK as sitk

def create_spherical_mask(subject):
  # Get the voxel from the physical space point
  LE_voxel = subject.T1.TransformPhysicalPointToIndex(subject.LE)
  RE_voxel = subject.T1.TransformPhysicalPointToIndex(subject.RE)
  # Eye diameter across vertically approx 18-19 mm
  # Eye diameter across horizontally approx 20 mm
  mask = subject.T1*0   # Create mask of image size
  mask[LE_voxel] = 1    # Set center of eye to 1
  dilated_image_LE = sitk.DilateImage(mask,10)  # Create 'sphere' for eye, r=10
  mask = subject.T1*0   # Repeat
  mask[RE_voxel] = 1
  dilated_image_RE = sitk.DilateImage(mask,10) # binary image

  mask_LE_RE = (dilated_image_LE, dilated_image_RE)

  return mask_LE_RE

def get_thresholds(subject,mask_LE_RE):
  # Get the threshold by multiplying the image by left and right eye masks
  T1_threshold = sitk.StatisticsImageFilter.execute(subject.T1*mask_LE_RE[0] + subject.T1*mask_LE_RE[1]).getMean()
  T2_threshold = sitk.StatisticsImageFilter.execute(subject.T2*mask_LE_RE[0] + subject.T2*mask_LE_RE[1]).getMean()
  return (T1_threshold, T2_threshold)


# Uses a spherical shape to create left eye and right eye masks w/ scaling
# 1 times LE and 2 times RE
def getTotalMask(subject):
  mask_LE_RE = create_spherical_mask(subject)
  return mask_LE_RE[0]*1 + mask_LE_RE[1]*2
