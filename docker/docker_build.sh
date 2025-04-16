PUSH=0
REPO=jeongyw12382/rampp
TAG=latest

while [[ "$#" -gt 0 ]]; do
    case $1 in
        --push) PUSH=1 ;;
        --tag) TAG=$2 ; shift ;;
        --repo) REPO=$2 ; shift ;;
    esac
    shift
done

echo "REPO: ${REPO}"
echo "TAG: ${TAG}"
echo "PUSH: ${PUSH}"


ls -l /var/run/docker.sock
docker build -t ${REPO}:${TAG} -f ./docker/Dockerfile .

if [[ $PUSH -eq 1 ]]; then
    docker push ${REPO}:${TAG}
fi