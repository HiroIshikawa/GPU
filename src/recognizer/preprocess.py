import cv2
import numpy as np


def region_of_interest(img, vertices):
    """Mask the region of given img to reduce object detection computation"""
    mask = np.zeros_like(img)
    if len(img.shape) > 2:
        channel_count = img.shape[2]
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def preprocess(img):
    """Preproces given image"""
    imshape = img.shape
    vertices = np.array([[
            (0,imshape[0]),
            (0,int(imshape[0]/2)),
            (int(imshape[1]),
            int(imshape[0]/2)),
            (imshape[1],imshape[0])]],
            dtype=np.int32)
    img = region_of_interest(img, vertices)
    return img
