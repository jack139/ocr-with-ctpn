# coding=utf-8
import os
import numpy as np

from ctpn import detect
import ocr

def get_images():
    files = []
    exts = ['jpg', 'png', 'jpeg', 'JPG']
    for parent, dirnames, filenames in os.walk('test_images/'):
        for filename in filenames:
            for ext in exts:
                if filename.endswith(ext):
                    files.append(os.path.join(parent, filename))
                    break
    print('Find {} images'.format(len(files)))
    return files


if __name__ == '__main__':

    im_fn_list = get_images()
    for im_fn in im_fn_list:
        img, boxes = detect.process_one(im_fn)

        # OCR 文字识别
        result = ocr.model(img, boxes)
        for key in result:
            print(result[key][1])

