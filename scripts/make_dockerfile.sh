#!/bin/sh

set -e

# Generate Dockerfile.
generate_docker() {
  docker run --rm jdkent/neurodocker:dev generate docker \
    --base=hbclab/accel-bids:unstable \
    --pkg-manager=apt \
    --user=coder \
    --workdir="/home/coder" \
    --env "SHELL=/bin/bash" \
    --run "curl -o /tmp/code-server.tar.gz -SL https://github.com/cdr/code-server/releases/download/3.0.2/code-server-3.0.2-linux-x86_64.tar.gz" \
    --run "mkdir -p /opt/codeserver && tar -xvf /tmp/code-server.tar.gz -C /opt/codeserver --strip-components=1" \
    --run '/opt/codeserver/code-server --install-extension eamodio.gitlens && /opt/codeserver/code-server --install-extension ms-python.python' \
    --expose 8080 \
    --entrypoint '/opt/codeserver/code-server --auth none --host 0.0.0.0 /home/coder/projects'

}

generate_docker > Dockerfile

docker build -t hbclab/accel-dev .
