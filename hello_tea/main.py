from PIL import Image
import numpy as np

def image_ghost(filepath):
    img_orig = Image.open(filepath) 


    array_orig = np.array(img_orig)

    array_r = np.copy(array_orig)
    array_r[:,:,1:3] = 0
    image_r = Image.fromarray(array_r)


    array_gb = np.copy(array_orig)
    array_gb[:,:,0] = 0
    image_gb = Image.fromarray(array_gb)



    canvas_r = Image.new("RGB", img_orig.size, color=(0,0,0))
    canvas_r.paste(image_r, (5, 5), image_r)


    canvas_gb = Image.new("RGB", img_orig.size, color=(0,0,0))
    canvas_gb.paste(image_gb,(0,0), image_gb)


    result_array = np.array(canvas_r) + np.array(canvas_gb)
    result = Image.fromarray(result_array)
    result.show()