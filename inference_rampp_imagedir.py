'''
 * The Recognize Anything Plus Model (RAM++)
 * Written by Xinyu Huang
'''
import argparse
from pathlib import Path
from tqdm import tqdm
import torch

from PIL import Image
from ram.models import ram_plus
from ram import inference_ram as inference
from ram import get_transform


parser = argparse.ArgumentParser(
    description='Tag2Text inferece for tagging and captioning')
parser.add_argument('--pretrained',
                    metavar='DIR',
                    help='path to pretrained model',
                    default='/data/checkpoints/rampp/ram_plus_swin_large_14m.pth')
parser.add_argument('--image-size',
                    default=384,
                    type=int,
                    metavar='N',
                    help='input image size (default: 448)')
parser.add_argument('--image-list',
                    metavar='DIR',
                    help='path to image list',
                    default='metadata/replica_ramplus_list.txt')

if __name__ == "__main__":

    args = parser.parse_args()

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    transform = get_transform(image_size=args.image_size)

    #######load model
    model = ram_plus(pretrained=args.pretrained,
                             image_size=args.image_size,
                             vit='swin_l')
    model.eval()

    model = model.to(device)


    with open(args.image_list, "r") as f:
        image_list = f.readlines()

    for image_info in tqdm(image_list):
        image_path, output_path = image_info.split()
        image = transform(Image.open(image_path)).unsqueeze(0).to(device)

        res = inference(image, model)
        objects = [object_name.strip() for object_name in res[0].split("|")]

        store_path = Path(output_path)
        store_path.parent.mkdir(parents=True, exist_ok=True)
        with open(store_path, 'w') as f:
            for object in objects:
                f.write(object + "\n")
