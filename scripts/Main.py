from utils.Mask import gen_mask, closure_function
from utils.ImageIO import get_subject, get_subject_list, Subject
from utils.thresholding import getTotalMask, get_thresholds
import SimpleITK as sitk
import os
import sys

def main():
    #directory = '/Volumes/easystore/PHD_NIFTI_NET_CONFIG/images/'
    directory = '/nfsscratch/Users/johnsonhj/StrokeLesion/DATA/images/'


    sub_list = get_subject_list(directory, sys.argv[1])

    for identifier in sub_list:
        output_file_name = os.path.join(directory,'{identifier}_eye_mask.nii.gz'.format(identifier=identifier))
        if not os.path.exists(output_file_name):
            sub = get_subject(identifier=identifier, directory=directory)
            eye_mask = getTotalMask(sub)
            t1_threshold, t2_threshold = get_thresholds(sub)
            total_mask = gen_mask(sub, eye_mask, t1_threshold, t2_threshold)
            print(output_file_name)
            sitk.WriteImage(sitk.Cast(total_mask, sitk.sitkUInt8),output_file_name)


if __name__ == '__main__':
    main()
