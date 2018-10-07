from matplotlib import pyplot as plt
import SimpleITK as sitk
from scripts.ImageIO import *

SLICE_INDEX = 1


def sliceImageAtEye(subject:Subject):
    t1_imag = subject.t1
    posterior_LE_index = t1_imag.TransformPhysicalPointToIndex(subject.LE)[SLICE_INDEX]
    size = subject.t1.GetSize()
    plt.imshow(sitk.GetArrayViewFromImage(t1_imag)[::-1, size[SLICE_INDEX] - posterior_LE_index, :])
    plt.show()
    print("Wrote image")


if __name__ == "__main__":
    path = "C:\\Users\\User\\OneDrive - University of Iowa\\Hackathons\\HackUIowa2018\\UIOWA2018_LesionMapping\\SmallData\\"
    subject_list = get_subject_list(path)
    subject = get_subject(subject_list[0], path)
    sliceImageAtEye(subject)