

def centering_img(img):
    """Calculate the center of image in (x,y)."""
    height, width, channels = img.shape
    center_x = width/2
    center_y = height/2
    return (center_x, center_y)


def sizing_box(rect):
    """Calculate the size of box."""
    box_width = abs(rect[0] - rect[2])
    box_height = abs(rect[1] - rect[3])
    return (box_width, box_height)


def centering_box(rect):
    """Calculate the (x,y) of the center of a box in the iamge."""
    box_x = abs(rect[0] - rect[2])/2 + rect[0]
    box_y = abs(rect[1] - rect[3])/2 + rect[1]
    return (box_x, box_y)


def pos_from_center(img_center, box_center):
    """Calcualte the relative position of the object"""
    box_rel_x = box_center[0]-img_center[0]
    box_rel_y = box_center[1]-img_center[1]
    return (box_rel_x, box_rel_y)


def measure(img, rects, candidates):
    """
    Measure the object location.

    Put an object with maximam size detected in a
    video frame (since cascade may detect more than
    one) into candidate list, which is examined
    regularly to initiate a command to arduino.
    """
    img_center = centering_img(img)
    num_boxes = len(rects)
    boxes = []
    for k in range(num_boxes):
        boxes.append({'box_id':0,'box_size': (0,0),'box_center':(0,0),'box_to_center':(0,0)})

    for i, rect in enumerate(rects):
        boxes[i]['box_id'] = i
        box_size = sizing_box(rect)
        boxes[i]['box_size'] = box_size
        box_center = centering_box(rect)
        boxes[i]['box_center'] = box_center
        box_to_center = pos_from_center(img_center, box_center)
        boxes[i]['box_to_center'] = box_to_center

    if (boxes):
        maxSizeItem = max(boxes, key=lambda x:x['box_size'][0]*x['box_size'][1])
        candidates.append(maxSizeItem['box_to_center'][0])
