import cv2
import numpy as np
import pickle
import PIL as Image
import matplotlib as plt
from keras_frcnn import config



def format_img(img, C):
    img_min_side = float(C.im_size)
    (height,width,_) = img.shape

    if width <= height:
        f = img_min_side/width
        new_height = int(f * height)
        new_width = int(img_min_side)
    else:
        f = img_min_side/height
        new_width = int(f * width)
        new_height = int(img_min_side)
    img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_CUBIC)
    img = img[:, :, (2, 1, 0)]
    img = img.astype(np.float32)
    img[:, :, 0] -= C.img_channel_mean[0]
    img[:, :, 1] -= C.img_channel_mean[1]
    img[:, :, 2] -= C.img_channel_mean[2]
    img /= C.img_scaling_factor
    img = np.transpose(img, (2, 0, 1))
    img = np.expand_dims(img, axis=0)
    return img

def get_data(input_path):
    found_bg = False
    all_imgs = {}

    classes_count = {}

    class_mapping = {}

    visualise = True

    with open(input_path,'r') as f:

        print('Parsing annotation files')

        for line in f:
            line_split = line.strip().split(',')
            (filename,x1,y1,x2,y2,class_name) = line_split
            print filename

            img = cv2.imread(filename)
            X = format_img(img,C)

            img_scaled = np.transpose(X.copy()[0, (2, 1, 0), :, :], (1, 2, 0)).copy()
            img_scaled[:, :, 0] += 123.68
            img_scaled[:, :, 1] += 116.779
            img_scaled[:, :, 2] += 103.939

            img_scaled = img_scaled.astype(np.uint8)

            (rows, cols) = img_scaled.shape[:2]
            print(rows, cols)
            print(x1,y1,x2,y2)

            if x1 < 0:
                x1 = 0
            if y1 < 0:
                y1 = 0
            if x2 < 0:
                x2 = 0
            if y2 < 0:
                y2 = 0

            roi = img_scaled[int(y1):int(y2), int(x1):int(x2)]
            (height,weight) = roi.shape[:2]
            print("Piexls: ",(height,weight))
            print("Area: ",(height*weight))
            #cv2.imshow('img',roi)
            #cv2.waitKey(0)

            try:
                with open("./Aresplot.txt", "a+") as f:
                    string = filename  + ',' + str(height*weight) + ',' + class_name + '\n'
                    #string = filename + ',' + str(height) + ',' +str(weight) + ',' + class_name + '\n'
                    f.write(string)
            except Exception as e:
                print(e)

        # make sure the bg class is last in the list
        if found_bg:
            if class_mapping['bg'] != len(class_mapping) - 1:
                key_to_switch = [key for key in class_mapping.keys() if class_mapping[key] == len(class_mapping)-1][0]
                val_to_switch = class_mapping['bg']
                class_mapping['bg'] = len(class_mapping) - 1
                class_mapping[key_to_switch] = val_to_switch

        return all_data, classes_count, class_mapping


with open("./config.pickle", 'r') as f_in:
    C = pickle.load(f_in)

(all_imgs, classes_count, class_mapping) = get_data("/home/iscas/Desktop/keras-frcnn/output.txt")
print all_imgs, classes_count, class_mapping


