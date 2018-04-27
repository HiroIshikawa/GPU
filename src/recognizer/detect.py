import cv2


def multi_detect(img, cascade_list, scale_factor, min_neighs):
    """Apply multiple cascade"""
    total_rects = []
    for cascade in enumarate(cascade_list):
        root = xml.etree.ElementTree.parse(cascade).getroot()
        width = root[0][3].text
        height = root[0][2].text
        rects = cascade.detectMultiScale(img, scale_factor, min_neighs, cv2.CASCADE_SCALE_IMAGE, (width,height))
        if len(rects) == 0:
            pass
        rects[:, 2:] += rects[:, :2]
        total_rects.extend(rects)
    return total_rects, img


def detect(img, scale_factor, min_neighs, obj_w, obj_h):
    """
    Detects objects that matches with cascade classifiers.

    The regions of target object detected get covered by
    rectangles. Each rect data contains: (x1, y1, x2, y2)
    """
    cascade = cv2.CascadeClassifier("model/cascade.xml")
    rects = cascade.detectMultiScale(img, scale_factor, min_neighs, cv2.CASCADE_SCALE_IMAGE, (obj_w,obj_h))
    if len(rects) == 0:
        return [], img
    rects[:, 2:] += rects[:, :2]
    return rects, img


def box(rects, img):
    """
    Draws box around the detected objects.

    The color and thickness of the line of box
    can be changed with the cv2.rectangle arguments.
    """
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), (127, 255, 0), 2)
    return img
