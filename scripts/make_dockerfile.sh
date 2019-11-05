#!/bin/sh

set -e

# Generate Dockerfile.
generate_docker() {
  docker run --rm jdkent/neurodocker:dev generate docker \
    --base=codercom/code-server:2.1472-vsc1.38.1 \
    --pkg-manager=apt \
    --user=coder \
    --workdir="/home/coder" \
    --env "SHELL=/bin/bash" \
    --copy . /home/coder/project \
    --miniconda create_env='accel' \
                yaml_file='/home/coder/project/environment.yml' \
    --run-bash "conda init && . /home/coder/.bashrc && . activate accel && pip install -e /home/coder/project" \
    --run 'code-server --install-extension eamodio.gitlens && code-server --install-extension ms-python.python' \
    --entrypoint 'code-server /home/coder/project'

}

generate_docker > Dockerfile

docker build -t hbclab/accel .