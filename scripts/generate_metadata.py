import argparse
from natsort import natsorted
from pathlib import Path

def generate_replica_metadata(path_to_dir):
    PATH_TO_ALL_SCENES = "./metadata/replica_all_scenes.txt"
    with open(PATH_TO_ALL_SCENES, "r") as f:
        all_scenes = f.readlines()

    out_texts = []

    for scene in all_scenes:
        scene = scene.strip()
        path_to_scene = Path(path_to_dir) / scene

        path_to_images = path_to_scene / "color"
        image_paths = list(path_to_images.glob("*.jpg")) + list(path_to_images.glob("*.png"))
        for image_path in natsorted(image_paths):
            name = image_path.stem
            name_wo_ext = name.split(".")[0]
            object_path = path_to_scene / "objects" / f"{name_wo_ext}.txt"
            out_texts.append(f"{image_path} {object_path}")


    with open(Path("metadata", "replica_ramplus_list.txt"), "w") as f:
        for text in out_texts:
            f.write(text + "\n")

def generate_metadata(dataset_name, path_to_dir):

    if dataset_name == "replica":
        generate_replica_metadata(path_to_dir)
    else:
        raise ValueError(f"Unsupported dataset: {dataset_name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset_name", type=str, choices=["replica"], default="replica")
    parser.add_argument("--path_to_dir", type=str, default="/data/3d_pcd/data/replica_2d")
    args = parser.parse_args()

    generate_metadata(args.dataset_name, args.path_to_dir)