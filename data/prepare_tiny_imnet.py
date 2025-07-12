import argparse
import os
import shutil
import tqdm

def restructure_val(data_path):
    # val_path = path + "val/"
    val_path = os.path.join(data_path, "val/")
    annotation_path = os.path.join(val_path, "val_annotations.txt")
    
    img_to_class = {}
    with open(annotation_path, "r") as f:
        lines = f.readlines()
    
    for line in lines:
        img_name, class_id = line.strip().split("\t")[:2]
        img_to_class[img_name] = class_id

    val_imgs_dir = os.path.join(val_path, "images")
    for img_name, class_id in tqdm.tqdm(img_to_class.items()):
        class_path = os.path.join(val_path, class_id)
        if not os.path.exists(class_path):
            os.mkdir(class_path)
        img_path = os.path.join(val_imgs_dir, img_name)
        dist_img_path = os.path.join(class_path, img_name)
        shutil.move(img_path, dist_img_path)
    
    shutil.rmtree(val_imgs_dir)
    os.remove(annotation_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--path",
        type = str,
        required = True,
        help = "Path to tiny-imagenet dataset"
    )
    args = parser.parse_args()
    restructure_val(args.path)
