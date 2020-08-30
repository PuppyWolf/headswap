import json
import os
import glob
from PIL import Image

keypoint_list = ["left_shoulder", "right_shoulder", "left_mouse", "right_mouse", "nose", "left_eye",
                 "right_eye", "left_ear", "right_ear", "chi"]


class KeyPoint:
    def __init__(self):
        pass

# load annotation
def load_keypoint_ann(file):
    with open(file , 'r') as f :
        ann = json.load(f)
        del ann['imageData']
    key2pos = {}
    for shape in ann['shapes']:
        keyp = shape['label']
        if keyp not in key2pos.keys():
            key2pos[keyp] = shape['points']
        else :
            key2pos[keyp].append( shape['points'][0])
    return key2pos

#
def load_img_and_ann(folder):
    dict_img_ann = {}
    for f in glob.glob(folder + "*.json"):
        ann = load_keypoint_ann(f)
        img_name = os.path.basename(f).split(".json")[0]
        #print(img_name)
        img = Image.open(  f.split(".json")[0] + '.jpg')
        dict_img_ann[img_name] = (img , ann)
    return dict_img_ann


from geometry_tools import line_segments_offset
if __name__ == '__main__':
    folder = "./测试素材/测试人物/"
    ann_folder = load_img_and_ann(folder)
    chi_points = ann_folder['4 (2)'][1]['chi']
    chi_points = sorted(chi_points ,key= lambda x : x[0])
    chi_offset = line_segments_offset(chi_points , 2 )