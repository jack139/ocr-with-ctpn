# coding=utf-8
import os
import numpy as np

from ctpn import detect
import ocr

#sys.path.append(os.getcwd()+'/ctpn')

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


    #boxes = np.array([np.array([  79,   59, 1264,   50,   80,  148, 1264,  139])])
    #boxes = np.array([np.array([  79,   52, 1024,   46, 1024,  115,   80,  122,    0])])

    #boxes = np.array([np.array([  79,   52, 1024,   46,   80,  122, 1024,  115])])
    #
    #print boxes
    #boxes = sort_box(boxes)
    #
    #print boxes
    #image = np.array(Image.open('test_result/test.jpg').convert('RGB'))
    #print image
    #result = charRec(image, boxes)
    #print result
