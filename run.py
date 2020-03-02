import cv2
import pydicom
import numpy as np
from matplotlib import pyplot as plt


def load_dcm(filename):
    return pydicom.dcmread(f'data/{filename}')


def main():
    dcm = load_dcm(filename='16351644_s1_CT_PETCT.dcm')

    img_dcm = dcm.pixel_array
    img_sagital = np.rot90(np.max(img_dcm, axis=2), k=-1)

    [print(f'{k}: {v}') for k, v in dcm.items()]
    plt.imshow(img_sagital, cmap=plt.cm.bone)
    plt.show()


if __name__ == '__main__':
    main()
