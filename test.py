import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread


def median_cut_quantize(img, img_arr):
    # when it reaches the end, color quantize
    print("start quantize: ", len(img_arr))
    r_average = np.mean(img_arr[:,0])
    g_average = np.mean(img_arr[:,1])
    b_average = np.mean(img_arr[:,2])
    # print('img_arr', img_arr)
    for data in img_arr:
        img[data[3]][data[4]] = [r_average, g_average, b_average] # set average color in bucket
    
def split_into_buckets(img, img_arr, depth):
    
    if len(img_arr) == 0:
        return 
        
    if depth == 0:
        median_cut_quantize(img, img_arr)
        return
    
    r_range = np.max(img_arr[:,0]) - np.min(img_arr[:,0])
    g_range = np.max(img_arr[:,1]) - np.min(img_arr[:,1])
    b_range = np.max(img_arr[:,2]) - np.min(img_arr[:,2])
    max_range_space = (0 if r_range*2>g_range+b_range else 1 if g_range*2>b_range+r_range else 2)

    # sort by color
    img_arr = img_arr[img_arr[:,max_range_space].argsort()]
    median_index = int((len(img_arr)+1)/2) # bucket split index
    print("median_index:", median_index)

    
    # split by median
    split_into_buckets(img, img_arr[0:median_index], depth-1)
    split_into_buckets(img, img_arr[median_index:], depth-1)
    



# ----------------------------------

sample_img = imread('images/hills.jpeg')
    
# list of pixels with their positions in image
flattened_img_array = []
for rindex, rows in enumerate(sample_img):
    for cindex, color in enumerate(rows):
        flattened_img_array.append([color[0],color[1],color[2],rindex, cindex]) 
print('len',len(flattened_img_array))


flattened_img_array = np.array(flattened_img_array)
split_into_buckets(sample_img, flattened_img_array, 1)

plt.imshow(sample_img)
plt.show()