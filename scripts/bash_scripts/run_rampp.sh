

DATASET_NAME=replica
PRETRAINED=/data/checkpoints/rampp/ram_plus_swin_large_14m.pth
PATH_DIR=/data/3d_pcd/data/replica_2d
METADATA_PATH=./metadata/replica_ramplus_list.txt

# Parse command line arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --dataset_name) DATASET_NAME=$2 ; 
            shift ;;
        --pretrained) PRETRAINED=$2 ; shift ;;
    esac
    shift
done

if [ ${DATASET_NAME} == "replica" ]; then
    # Generate metadata
    PATH_DIR=/data/3d_pcd/data/replica_2d ;
    METADATA_PATH=./metadata/replica_ramplus_list.txt
elif [ ${DATASET_NAME} == "scannet" ]; then
    PATH_DIR=/data/3d_pcd/data/scannet_2d ;
    METADATA_PATH=./metadata/scannetv2_ramplus_list.txt
fi

python3 -m scripts.generate_metadata --dataset_name ${DATASET_NAME} --path_to_dir ${PATH_DIR}
python3 -m inference_rampp_imagedir --pretrained ${PRETRAINED} --image-list ${METADATA_PATH}