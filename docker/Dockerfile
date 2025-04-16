# Use an official NVIDIA CUDA base image (choose the version you need)
FROM nvidia/cuda:12.4.0-base-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install Python and other dependencies as needed
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        curl \
        wget \
        git \
        vim \
        htop \
        unzip \
        software-properties-common \
        locales \
        python3 \
        python3-pip \
        python3-venv \
        tmux \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install tqdm
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Set default command to check GPU visibility
CMD ["nvidia-smi"]
