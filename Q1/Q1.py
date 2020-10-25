import json
import cv2
import numpy as np


def getRec(file_path):
    with open(file_path,'r') as load_f:
        jsonFile = json.load(load_f)
        # print(jsonFile['boxes'])
        for it in jsonFile['boxes']:
            if it['name']=='box_b':
                print('box_b: ', it['rectangle'])
                return it['rectangle']


def paddingImg(background_path, img_path, target_area):
    wait_time = 0
    bg = cv2.imread(background_path)
    bg_size = bg.shape
    print('bg size: ', bg_size)

    output = bg
    cv2.imshow('bg.jpg', bg)
    cv2.waitKey(wait_time)

    try:
        img = cv2.imread(img_path)
        img_size = img.shape
        print('img size: ', img_size)
        cv2.imshow('img.jpeg', img)
        cv2.waitKey(wait_time)
    except:
        print('wrong img!')

    left = target_area['left_top'][0]
    top = target_area['left_top'][1]
    right = target_area['right_bottom'][0]
    bottom = target_area['right_bottom'][1]
    if img_size[2]==bg_size[2]==3:
        if img_size[0]<=bg_size[0] and img_size[1]<=bg_size[1]:
            output[top:bottom, left:right] = img
        else:
            img_resize = cv2.resize(img, (right-left, bottom-top), interpolation=cv2.INTER_CUBIC)
            output[top:bottom, left:right] = img_resize

    cv2.imshow('output.jpg', output)
    cv2.waitKey(wait_time)

    # htitch = np.hstack([bg, img, output])
    # cv2.imshow('output.jpg', htitch)
    # cv2.waitKey(wait_time)

if __name__ == '__main__':
    file_path = 'files/boxes.json'
    box_b = getRec(file_path)

    background_path = 'imgs/bg.jpg'
    img_path = 'imgs/dog.jpeg'
    paddingImg(background_path, img_path, box_b)






