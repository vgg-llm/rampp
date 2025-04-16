IMAGE=jeongyw12382/rampp:latest
NAME=rampp

while [[ "$#" -gt 0 ]]; do
    case $1 in
        --image) IMAGE=$2 ; shift ;;
        --name) NAME=$2 ; shift ;;
    esac
    shift
done

docker run -itd \
    -p 8080:8080 \
    -v /home/yoonwoo/datasets:/data \
    -v ${PWD}:/workspace \
    --gpus all \
    --shm-size=16G \
    --name ${NAME} \
    ${IMAGE} bash
